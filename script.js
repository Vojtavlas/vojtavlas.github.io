const fileInput = document.getElementById('fileInput');
const encryptButton = document.getElementById('encryptButton');
const decryptButton = document.getElementById('decryptButton');
const downloadLink = document.getElementById('downloadLink');
const keyDisplay = document.getElementById('keyDisplay');
const copyKeyButton = document.getElementById('copyKeyButton');
let selectedFile;
let encryptionMode = true;

fileInput.addEventListener('change', (event) => {
    selectedFile = event.target.files[0];
    if (selectedFile) {
        encryptButton.disabled = false;
        decryptButton.disabled = false;
        copyKeyButton.disabled = true;
        keyDisplay.textContent = 'Generating key...';
    } else {
        encryptButton.disabled = true;
        decryptButton.disabled = true;
        copyKeyButton.disabled = true;
        keyDisplay.textContent = '';
    }
});

encryptButton.addEventListener('click', async () => {
    encryptionMode = true;
    processFile();
});

decryptButton.addEventListener('click', async () => {
    encryptionMode = false;
    processFile();
});

async function processFile() {
    if (!selectedFile) {
        return;
    }

    const key = await window.crypto.subtle.generateKey(
        {
            name: 'AES-CBC',
            length: 256
        },
        true,
        ['encrypt', 'decrypt']
    );

    const keyBuffer = await window.crypto.subtle.exportKey('raw', key);
    const keyArray = Array.from(new Uint8Array(keyBuffer));
    const keyHex = keyArray.map(byte => byte.toString(16).padStart(2, '0')).join('');
    keyDisplay.textContent = 'Key: ' + keyHex;
    copyKeyButton.disabled = false;

    const iv = window.crypto.getRandomValues(new Uint8Array(16));
    const fileBuffer = await selectedFile.arrayBuffer();
    let data;
    if (encryptionMode) {
        data = await window.crypto.subtle.encrypt({ name: 'AES-CBC', iv }, key, fileBuffer);
    } else {
        data = await window.crypto.subtle.decrypt({ name: 'AES-CBC', iv }, key, fileBuffer);
    }

    const blobType = encryptionMode ? 'application/octet-stream' : selectedFile.type;
    const fileName = encryptionMode ? `${selectedFile.name}.aes` : selectedFile.name.replace('.aes', '');
    downloadLink.href = URL.createObjectURL(new Blob([iv, data], { type: blobType }));
    downloadLink.download = fileName;
    downloadLink.style.display = 'block';
}
