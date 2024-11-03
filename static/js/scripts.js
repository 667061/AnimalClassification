// static/js/scripts.js

let dropArea = document.getElementById('drop-area');
let gallery = document.getElementById('gallery');

// Prevent default browser actions for drag-and-drop events
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

// Highlight drop area when item is dragged over it
['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, () => dropArea.classList.add('hover'), false);
});

['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, () => dropArea.classList.remove('hover'), false);
});

// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false);

function handleDrop(e) {
    let files = e.dataTransfer.files;
    handleFiles(files);
}

function handleFiles(files) {
    files = [...files];
    files.forEach(uploadFile);
    files.forEach(previewFile);
}

function previewFile(file) {
    let reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onloadend = function() {
        let img = document.createElement('img');
        img.src = reader.result;
        // Prepend the new image to the gallery
        gallery.insertBefore(img, gallery.firstChild);
    }
}

function uploadFile(file) {
    let url = '/upload';
    let formData = new FormData();
    formData.append('file', file);

    fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            let result = document.createElement('div');
            // Format probability as a percentage with one decimal point
            let confidence = (data.confidence * 100).toFixed(1);
            result.textContent = `Animal: ${data.class}  | Confidence: ${confidence}%`;
            // Prepend the result to the gallery
            gallery.insertBefore(result, gallery.firstChild);
        }
    })
    .catch(err => {
        console.error(err);
        alert('An error occurred while uploading the file.');
    });
}
