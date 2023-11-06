const fileInput = document.getElementById("file-input");
const fileInfo = document.getElementById("file-info");
const fileName = document.getElementById("file-name");
const fileType = document.getElementById("file-type");
const fileSize = document.getElementById("file-size");

document.getElementById("file-upload-form").addEventListener("submit", (e) => {
    e.preventDefault();

    const file = fileInput.files[0];
    if (file) {
        fileName.textContent = file.name;
        fileType.textContent = file.type;
        fileSize.textContent = (file.size / 1024).toFixed(2) + " KB";
    } else {
        fileInfo.innerHTML = "<p>No file selected.</p>";
    }
});
