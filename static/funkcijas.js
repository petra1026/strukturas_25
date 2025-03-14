const LAIKS = 5000;

async function suutiitZinju() {
    const zinja = document.getElementById("teksts").value;
    const vards = document.getElementById("vards").value;
    
    if (!zinja.trim() || !vards.trim()) {
        alert("Lūdzu, aizpildiet gan vārdu, gan ziņu!");
        return;
    }

    try {
        document.getElementById("teksts").value = "";
        const atbilde = await fetch('/jschats/suutiit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json; charset=utf-8'
            },
            body: JSON.stringify({
                "saturs": zinja,
                "vards": vards
            })
        });

        if (!atbilde.ok) {
            throw new Error('Neizdevās nosūtīt ziņu');
        }
    } catch (error) {
        alert('Kļūda: ' + error.message);
    }
}

async function lasiitZinju() {
    try {
        const atbilde = await fetch("/jschats/lasiit");
        if (!atbilde.ok) {
            throw new Error('Neizdevās ielādēt ziņas');
        }
        const zinas = await atbilde.json();
        raadiitZinjas(zinas);
        await new Promise(resolve => setTimeout(resolve, LAIKS));
        await lasiitZinju();
    } catch (error) {
        console.error('Kļūda:', error);
        await new Promise(resolve => setTimeout(resolve, LAIKS));
        await lasiitZinju();
    }
}

function raadiitZinjas(saturs) {
    const vieta = document.getElementById("chats");
    let teksts = "";
    
    for (const rinda of saturs) {
        const [vards, zinja] = rinda.split("----");
        teksts += `<div class="chat-message">
            <b>${vards}</b> - ${zinja}
        </div>`;
    }
    
    vieta.innerHTML = teksts;
}