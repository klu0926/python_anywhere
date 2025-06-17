const BACKEND_URL = window.location.hostname === 'localhost'
  ? 'http://127.0.0.1:5000'
  : 'https://klu0926.pythonanywhere.com';


document.addEventListener('DOMContentLoaded', () => {
  const fileInput = document.getElementById('fileInput');
  const preview = document.getElementById('preview');
  const convertBtn = document.getElementById('convertBtn');
  const asciiOutput = document.getElementById('asciiOutput');
  const previewDisplay = document.getElementById('preview-display')
  const widthSelector = document.getElementById('width-selector')
  const copyButton = document.getElementById('output-copy')
  const copyButtonMessage = document.getElementById('output-copy-message')

  // Show image preview
  fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    preview.src = file ? URL.createObjectURL(file) : '';
    previewDisplay.style.display = 'block'
  });

  // Convert button click
  convertBtn.addEventListener('click', async () => {
    if (!fileInput.files[0]) {
      alert('Please upload an image.');
      return;
    }

    const formData = new FormData();
    // Name the image file 'image'
    formData.append('image', fileInput.files[0]);

    // Get width input from width-selector
    formData.append('width', widthSelector.value)

    // Display for loading
    asciiOutput.textContent = 'Converting...';

    try {
      const response = await fetch(`${BACKEND_URL}/ascii/upload`, {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();

      // Display ASCII art
      asciiOutput.textContent = data.ascii || `Error: ${data.error}`;
    } catch (err) {
      asciiOutput.textContent = 'Network error or server not reachable.';
    }
  });


  // Copy button
  copyButton.addEventListener('click', () => {

    // Get value from output
    const text = asciiOutput.textContent

    if (text.trim() === '') return

    // Copy to clipboard
    navigator.clipboard.writeText(text).then(() => {
      // Do something when is copied
      copyButtonMessage.innerText = 'Copied'
    }).catch(err => {
      // Display text
      copyButtonMessage.innerText = 'Fail to copy'
    })
  })

});
