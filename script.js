const fileInput = document.getElementById('fileInput');
const fileInfo = document.getElementById('fileInfo');

fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        const fileName = file.name;
        const fileSize = Math.round(file.size / 1024) + ' KB';
        const fileType = file.type || 'n/a';
        fileInfo.textContent = `File Name: ${fileName}\nFile Size: ${fileSize}\nFile Type: ${fileType}`;
    } else {
        fileInfo.textContent = 'No file selected';
    }
});
