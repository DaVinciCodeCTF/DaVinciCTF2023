import socket
from flask import *
from web3 import Web3
from web3.middleware import geth_poa_middleware
from pygments import highlight
from pygments.lexers import (get_lexer_by_name, get_lexer_for_filename, get_lexer_for_mimetype, JsonLexer)
from pygments.formatters import HtmlFormatter
from subprocess import run, CalledProcessError
from os import chdir
from flask_socketio import SocketIO, emit
import re

app = Flask(__name__)
socketio = SocketIO(app)

deploy_directory = "/home/dovahshan/DVC_blockchain/deploy"

@app.route('/')
def home():
    client = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    #blocknumber = client.eth.get_block('latest').number
    #Supplies = "{:.2e}".format(client.eth.get_balance(Web3.toChecksumAddress("0x68124ed2a425e9ec16083c8322058dd5a4193466")))
    return render_template('home.html')

@app.route('/faucet')
def send_faucet():
    return render_template('faucet.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/challenge1')
def challenge1():
    challenge = open("../deploy/contracts/challenge1.sol", 'r').read()
    htmlcode = highlight(challenge, get_lexer_by_name('solidity'), HtmlFormatter(style='monokai', full=True))
    return render_template('challenge1.html', challenge=htmlcode)

@app.route('/challenge2')
def  challenge2():
    casino = open("../deploy/contracts/casino.sol", 'r').read()
    proxy = open("../deploy/contracts/proxy.sol", 'r').read()
    htmlcode1 = highlight(casino, get_lexer_by_name('solidity'), HtmlFormatter(style='monokai', full=True))
    htmlcode2 = highlight(proxy, get_lexer_by_name('solidity'), HtmlFormatter(style='monokai', full=True))
    return render_template('challenge2.html', casino=htmlcode1, proxy=htmlcode2)

##
##  On deploy
##
@socketio.on('deploy')
def challenges_deploy(message):
    print(message['data'])
    challenge = message['data']

    emit(f"{challenge}status" , {"output": "⬣ Deploying...", "state": 1, "address" : ""})

    deploy_script = ""
    if challenge == "challenge1":
        deploy_script = "deploy1"
        try:
            chdir(deploy_directory)
            print(f'truffle migrate')
            process = run(f'truffle migrate --f 1 --to 1 --network DVC', shell=True, check=True, capture_output=True)
            process = process.stdout.decode()
            address_index = process.find("The challenge 1 address is : ")
            address_info = process[address_index:].split()[6]
            print(process)
            emit(f"{challenge}status" , {"output": f"⬣ Deployed", "state": 2, "address" : f"{address_info}"})

        except CalledProcessError as e:
            emit(f"{challenge}status" , {"output": "⬣ Error", "state" : 3})
            print(e)

        finally:
            chdir("/home/dovahshan/DVC_blockchain/website/")
    elif challenge == "challenge2":
        deploy_script = "deploy2"
        try:
            chdir(deploy_directory)
            print(f'truffle migrate')
            process = run(f'truffle migrate --f 2 --to 2 --network DVC', shell=True, check=True, capture_output=True)
            process = process.stdout.decode()
            casino_index = process.find("The casino address is : ")
            casino_info = process[casino_index:].split()[5]
            proxy_index = process.find("The proxy address is : ")
            proxy_info = process[proxy_index:].split()[5]
            print(casino_info)
            print(proxy_info)
            emit(f"{challenge}status" , {"output": f"⬣ Deployed", "state": 2, "casino_address" : f"{casino_info}", "proxy_address" : f"{proxy_info}"})

        except CalledProcessError as e:
            emit(f"{challenge}status" , {"output": "⬣ Error", "state" : 3})
            print(e)

        finally:
            chdir("/home/dovahshan/DVC_blockchain/website/")
        
    else:

        for i in range(5):
            emit(f"challenge{i}deploystatus" , {"output": f"Not a challenge"})
            return
    

##
##  On verify
##
@socketio.on('verify')
def challenges_verify(message):
    print(message['data'])
    challenge = message['data']
    challenge_address = message['address'].strip('\n')
    emit(f"{challenge}status" , {"output": "⬣ Verifying", "state" : 4})
    client = Web3(Web3.HTTPProvider(f'http://127.0.0.1:7545'))
    # pooooowned
    if challenge == "challenge1":
        challenge_address = Web3.toChecksumAddress(challenge_address)
        print(challenge_address)
        client.middleware_onion.inject(geth_poa_middleware, layer=0)
        balance = client.eth.getBalance(challenge_address)
        if balance != 0:
            emit(f"{challenge}status" , {"output": f"⬣ FAILED !", "state": 3})
        else:
            emit(f"{challenge}status" , {"output": "dvCTF{Wh3r3D1DMyMon3YW3nt}", "state": 5})
    if challenge == "challenge2":
        verification_address = str(challenge_address[0:42])
        proxy_address = str(challenge_address[42:])
        print(proxy_address )
        print(verification_address)
        proxy_address = Web3.toChecksumAddress(proxy_address)
        verification_address = Web3.toChecksumAddress(verification_address)
        print("proxy_address", proxy_address)
        client.middleware_onion.inject(geth_poa_middleware, layer=0)
        proxy_contract = client.eth.contract(address=proxy_address, abi=open('./abis/02.json').read())
        won = proxy_contract.functions.getOwner().call()
        if won != verification_address:
            emit(f"{challenge}status" , {"output": f"⬣ FAILED !", "state": 3})
        else:
            emit(f"{challenge}status" , {"output": "dvCTF{Th3C451n0iSB4c7L4dy54ndG3ntl3m3n}", "state": 5})


##
##  On faucet
##
@socketio.on('get_money')
def get_money(message):
    address = message['data']
    print(address)
    #if not re.match('^0x[a-fA-F0-9]{40}$'):
     #   print("NO match")
      #  return
    try:
        chdir(deploy_directory)
        print(f'node sendmoney.js {address[:42]}')
        process = run(f'node sendmoney.js {address[:42]} ', shell=True, check=True, capture_output=True)
        output = process.stdout.decode()
        print(output)
        if "Error" in output:
            emit(f"faucetstatus" , {"output": f"⬣ Faucet error (too much money or is chain is down ?)", "state": 0})
            return
        emit(f"faucetstatus" , {"output": f"⬣ You're rich bro !", "state": 1})
    except CalledProcessError as e:
        print(e.output)
        print("ERROR")



# ##
# ##  Utiities
# ##
# def get_stats():
#     client = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
#     client.middleware_onion.inject(geth_poa_middleware, layer=0)
#     blocknumber = client.eth.get_block('latest').number
#     melSupplies = "{:.2e}".format(client.eth.get_balance(Web3.toChecksumAddress("0x68124ed2a425e9ec16083c8322058dd5a4193466")))

#     return (blocknumber, melSupplies)

# def get_visu():
#     client = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
#     client.middleware_onion.inject(geth_poa_middleware, layer=0)
#     curr_block = dict(client.eth.get_block('latest'))
#     # Lol ?
#     del curr_block["transactions"]
#     return curr_block

socketio.run(app, host="0.0.0.0", port=22000)