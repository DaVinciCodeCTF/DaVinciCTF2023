let dashboard = document.getElementById('dashboard');
if (isAdmin) {
    let p = document.createElement("p");
    p.innerText = "Admin dashboard";

    dashboard.appendChild(p);

    let f = document.createElement("form");
    f.setAttribute('method',"get");
    f.setAttribute('action',"/admin/dashboard/add");
    
    let i = document.createElement("input"); //input element, text
    i.setAttribute('type',"text");
    i.setAttribute('name',"username");
    i.setAttribute('id', "username_field");
    f.appendChild(i);

    let br = document.createElement("br");
    let br2 = document.createElement("br");
    f.appendChild(br);
    f.appendChild(br2);

    let b = document.createElement("button");
    b.innerText = 'OK';
    f.appendChild(b);

    dashboard.appendChild(f);

    let br3 = document.createElement("br");
    dashboard.appendChild(br3);

    let b2 = document.createElement("button");
    b2.innerText = 'Flag';
    b2.setAttribute('onclick', 'window.location="/flag"');
    dashboard.appendChild(b2);
} else {
    dashboard.innerText = 'Access denied';
}