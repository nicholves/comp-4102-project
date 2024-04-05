import React from 'react';

function App() {

  function handleFileChange(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = function(e) {
      const img = document.createElement("img");
      img.src = e.target.result;
      img.width = 200;
      document.getElementById("fileUpload").appendChild(img);
    }
    reader.readAsDataURL(file);
  }

  function handleScanButtonClick() {
    // make a request to the server to scan the image
    const formData = new FormData();
    const file = document.querySelector('#image').files[0];
    formData.append('image', file);
    console.log(formData);

    fetch('http://localhost:5000/upload', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('nutritionLabelJson').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => {
      console.error('Error:', error);
    });
    
  }

  return (
    <div className="App">
      <h1>Nutrition Label Scanner Test App</h1>
      <h2>Scan a nutrition label to get the nutrition facts</h2>
      <div id='fileUpload'>
        <input id='image' type="file" onChange={handleFileChange} />
      </div>
      <div style={{marginTop: '20px'}}>
        <button onClick={handleScanButtonClick}>Scan</button>
      </div>

      {/* View Nutrition Label JSON */}
      <div>
        <h2>Nutrition Label JSON</h2>
        <pre id="nutritionLabelJson"></pre>
      </div>

    </div>
  );
}

export default App;
