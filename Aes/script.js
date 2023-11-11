const fileInput = document.getElementById("file-input");
const fileInfo = document.getElementById("file-info");
const fileName = document.getElementById("file-name");
const fileType = document.getElementById("file-type");
const fileSize = document.getElementById("file-size");
const renameButton = document.getElementById("rename-button");
const downloadButton = document.getElementById("download-button");

document.getElementById("file-upload-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {
        const response = await fetch("/upload", {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            displayFileInfo();
        }
    } catch (error) {
        console.error("Error uploading file: " + error);
    }
});

renameButton.addEventListener("click", async () => {
    try {
        const response = await fetch("/rename", {
            method: "GET",
        });

        if (response.ok) {
            alert("File renamed successfully");
        }
    } catch (error) {
        console.error("Error renaming file: " + error);
    }
});

downloadButton.addEventListener("click", () => {
    window.location.href = "/download";
});

function displayFileInfo() {
    const file = fileInput.files[0];
    if (file) {
        fileName.textContent = file.name;
        fileType.textContent = file.type;
        fileSize.textContent = (file.size / 1024).toFixed(2) + " KB";
    } else {
        fileInfo.innerHTML = "<p>No file selected.</p>";
    }
}
