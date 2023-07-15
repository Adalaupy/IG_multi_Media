function handleFileSelect() {
			
    // Get a reference to the file input
    var fileInput = document.getElementById('pictures');

    // Get a reference to the preview container
    var previewContainer = document.getElementById('preview');
    previewContainer.innerHTML = '';

    // Loop through each selected file
    for (var i = 0; i < fileInput.files.length; i++) {
        var file = fileInput.files[i];


        // Create a preview item for images
        if (file.type.startsWith('image/') || file.name.endsWith('.cr2') ) {
            var previewItem = document.createElement('div');
            previewItem.className = 'preview-item';
            preview.height = 100
            previewItem.style.backgroundImage = 'url(' + URL.createObjectURL(file) + ')';
            previewContainer.appendChild(previewItem);
        }

        // Create a preview item for videos
        else if (file.type.startsWith('video/')) {
            var previewItem = document.createElement('video');
            previewItem.className = 'preview-item';
            previewItem.src = URL.createObjectURL(file);
            previewItem.controls = true;
            previewContainer.appendChild(previewItem);
        }
    }
}