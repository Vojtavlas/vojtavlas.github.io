const fileInput = document.getElementById('fileInput');
const encryptButton = document.getElementById('encryptButton');
const downloadLink = document.getElementById('downloadLink');
const keyDisplay = document.getElementById('keyDisplay');
const copyKeyButton = document.getElementById('copyKeyButton');
let selectedFile;

fileInput.addEventListener('change', (event) => {
    selectedFile = event.target.files[0];
    if (selectedFile) {
        encryptButton.disabled = false;
        copyKeyButton.disabled = true;
        keyDisplay.textContent = 'Generating key...';
    } else {
        encryptButton.disabled = true;
        copyKeyButton.disabled = true;
        keyDisplay.textContent = '';
    }
});

encryptButton.addEventListener('click', async () => {
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
    keyDisplay.textContent = 'Encryption Key: ' + keyHex;
    copyKeyButton.disabled = false;

    const iv = window.crypto.getRandomValues(new Uint8Array(16));
    const fileBuffer = await selectedFile.arrayBuffer();
    const encryptedData = await window.crypto.subtle.encrypt({ name: 'AES-CBC', iv }, key, fileBuffer);

    const encryptedBlob = new Blob([iv, encryptedData], { type: 'application/octet-stream' });
    const encryptedFileName = `${selectedFile.name}.aes`;
    downloadLink.href = URL.createObjectURL(encryptedBlob);
    downloadLink.download = encryptedFileName;
    downloadLink.style.display = 'block';
});

copyKeyButton.addEventListener('click', () => {
    const keyHex = keyDisplay.textContent.split(': ')[1];
    const textarea = document.createElement('textarea');
    textarea.value = keyHex;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
});
