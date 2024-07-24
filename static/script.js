document.getElementById('trainButton').addEventListener('click', () => {
    const spinner = document.getElementById('spinner');
    spinner.style.display = 'block';

    fetch('/train', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({}),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch((error) => {
        console.error('Error:', error);
    })
    .finally(() => {
        spinner.style.display = 'none';
    });
});

document.getElementById('predictButton').addEventListener('click', () => {
    const imageUpload = document.getElementById('imageUpload').files[0];

    if (imageUpload) {
        const formData = new FormData();
        formData.append('file', imageUpload);

        fetch('/predict', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('resultText').textContent = `Prediction: ${data.prediction}`;
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    } else {
        alert('Please upload an image first.');
    }
});

function previewImage(event) {
    const imagePreview = document.getElementById('imagePreview');
    imagePreview.innerHTML = ''; // Clear any existing content

    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        const img = document.createElement('img');
        img.src = e.target.result;
        imagePreview.appendChild(img);
    };

    if (file) {
        reader.readAsDataURL(file);
    }
}
