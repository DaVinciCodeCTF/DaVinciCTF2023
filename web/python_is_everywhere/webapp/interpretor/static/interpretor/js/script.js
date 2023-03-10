async function executePython() {
    await new Promise(resolve => setTimeout(resolve, 100));
    document.getElementById('runButton').click();
}

async function fillPython() {
    await new Promise(resolve => setTimeout(resolve, 100));
    const params = new URLSearchParams(window.location.search);
    const pythonCode = params.get('python');
    if (pythonCode && pythonCode.length !== 0) {
        document.getElementsByClassName('cm-activeLine')[0].innerHTML = atob(pythonCode);
        executePython();
    }
}

