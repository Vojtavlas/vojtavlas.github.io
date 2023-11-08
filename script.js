const fileInput = document.getElementById('fileInput');
const encryptButton = document.getElementById('encryptButton');
const decryptButton = document.getElementById('decryptButton');
const downloadLink = document.getElementById('downloadLink');
const keyDisplay = document.getElementById('keyDisplay');
const customKeyInput = document.getElementById('customKey');
const copyKeyButton = document.getElementById('copyKeyButton');
let selectedFile;

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
    decryptButton.disabled = true;
    copyKeyButton.disabled = false; // Enable copy button for encryption
    processFile(false);
});

decryptButton.addEventListener('click', async () => {
    encryptButton.disabled = true;
    copyKeyButton.disabled = true; // Disable copy button for decryption
    processFile(true);
});

customKeyInput.addEventListener('input', () => {
    keyDisplay.textContent = '';
    copyKeyButton.disabled = true;
});

async function generateKey() {
    const key = await window.crypto.subtle.generateKey(
        {
            name: 'AES-CBC',
            length: 256
        },
        true,
        ['encrypt', 'decrypt']
    );
    return key;
}

async function processFile(decryptionMode) {
    if (!selectedFile) {
        return;
    }

    const keyHex = customKeyInput.value;

    if (!keyHex) {
        keyDisplay.textContent = 'Custom key is required';
        return;
    }

    const keyData = new TextEncoder().encode(keyHex);

    if (keyData.length !== 32) { // 256-bit key length
        keyDisplay.textContent = 'Custom key must be 32 characters (256 bits)';
        return;
    }

    const key = await window.crypto.subtle.importKey(
        'raw',
        keyData,
        { name: 'AES-CBC' },
        true,
        ['encrypt', 'decrypt']
    );

    keyDisplay.textContent = 'Key: ' + keyHex;

    const iv = window.crypto.getRandomValues(new Uint8Array(16));
    const fileBuffer = await selectedFile.arrayBuffer();
    let data;

    if (decryptionMode) {
        data = await window.crypto.subtle.decrypt({ name: 'AES-CBC', iv }, key, fileBuffer);
    } else {
        data = await window.crypto.subtle.encrypt({ name: 'AES-CBC', iv }, key, fileBuffer);
    }

    const blobType = decryptionMode ? selectedFile.type : 'application/octet-stream';
    const fileName = decryptionMode ? selectedFile.name.replace('.aes', '') : `${selectedFile.name}.aes`;
    downloadLink.href = URL.createObjectURL(new Blob([iv, data], { type: blobType }));
    downloadLink.download = fileName;
    downloadLink.style.display = 'block';
}

// Generate key when the page loads
generateKey().then(() => {
    keyDisplay.textContent = 'Generating key...';
});
