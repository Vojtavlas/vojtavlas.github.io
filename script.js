const fileInput = document.getElementById('fileInput');
const encryptButton = document.getElementById('encryptButton');
const downloadLink = document.getElementById('downloadLink');
let selectedFile;

fileInput.addEventListener('change', (event) => {
    selectedFile = event.target.files[0];
    if (selectedFile) {
        encryptButton.disabled = false;
    } else {
        encryptButton.disabled = true;
    }
});

encryptButton.addEventListener('click', async () => {
    if (!selectedFile) {
        return;
    }

    const password = prompt('Enter a password for encryption:');
    if (!password) {
        return;
    }

    const fileBuffer = await selectedFile.arrayBuffer();
    const cryptoKey = await window.crypto.subtle.importKey('raw', new TextEncoder().encode(password), 'AES-CBC', false, ['encrypt']);
    const iv = window.crypto.getRandomValues(new Uint8Array(16));
    const encryptedData = await window.crypto.subtle.encrypt({ name: 'AES-CBC', iv }, cryptoKey, fileBuffer);

    const encryptedBlob = new Blob([iv, encryptedData], { type: 'application/octet-stream' });
    const encryptedFileName = `${selectedFile.name}.aes`;
    downloadLink.href = URL.createObjectURL(encryptedBlob);
    downloadLink.download = encryptedFileName; // Set the download attribute
    downloadLink.style.display = 'block';
});
