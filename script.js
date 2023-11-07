const fileInput = document.getElementById('fileInput');
const newFileNameInput = document.getElementById('newFileName');
const downloadButton = document.getElementById('downloadButton');
const fileInfo = document.getElementById('fileInfo');

let selectedFile;

fileInput.addEventListener('change', (event) => {
    selectedFile = event.target.files[0];
    if (selectedFile) {
        const fileName = selectedFile.name;
        const fileSize = Math.round(selectedFile.size / 1024) + ' KB';
        const fileType = selectedFile.type || 'n/a';
        fileInfo.textContent = `File Name: ${fileName}\nFile Size: ${fileSize}\nFile Type: ${fileType}`;
        downloadButton.disabled = false;
    } else {
        fileInfo.textContent = 'No file selected';
        downloadButton.disabled = true;
    }
});

downloadButton.addEventListener('click', () => {
    if (selectedFile) {
        const newFileName = newFileNameInput.value || selectedFile.name;
        const downloadLink = document.createElement('a');
        downloadLink.href = URL.createObjectURL(selectedFile);
        downloadLink.download = newFileName;
        downloadLink.click();
    }
});
