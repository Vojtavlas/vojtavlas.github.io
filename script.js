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
        keyDisplay.textContent = 'Key: Hard-codedDemoKey';
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

    const keyHex = 'Hard-codedDemoKey';

    const iv = window.crypto.getRandomValues(new Uint8Array(16));
    const fileBuffer = await selectedFile.arrayBuffer();
    const encryptedData = await window.crypto.subtle.encrypt({ name: 'AES-CBC', iv }, new TextEncoder().encode(keyHex), fileBuffer);

    const encryptedBlob = new Blob([iv, encryptedData], { type: 'application/octet-stream' });
    const encryptedFileName = `${selectedFile.name}.aes`;
    downloadLink.href = URL.createObjectURL(encryptedBlob);
    downloadLink.download = encryptedFileName;
    downloadLink.style.display = 'block';
});

copyKeyButton.addEventListener('click', () => {
    const keyHex = 'Hard-codedDemoKey';
    const textarea = document.createElement('textarea');
    textarea.value = keyHex;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
});
