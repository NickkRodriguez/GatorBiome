<template>
    <div class="uploader-container">
      <h1>GatorBiome File Upload Test</h1>
      
      <div class="upload-section">
        <h2>Single CSV Upload</h2>
        <div class="file-input">
          <input type="file" accept=".csv" @change="onSingleFileChange" />
          <button @click="uploadSingleFile" :disabled="!singleFile">Upload CSV</button>
        </div>
        <div v-if="singleFileResult" class="result">
          <h3>Upload Result:</h3>
          <pre>{{ singleFileResult }}</pre>
        </div>
      </div>
  
      <div class="upload-section">
        <h2>Dataset Upload (Train & Test)</h2>
        <div class="file-input">
          <div>
            <label>Train CSV:</label>
            <input type="file" accept=".csv" @change="onTrainFileChange" />
          </div>
          <div>
            <label>Test CSV:</label>
            <input type="file" accept=".csv" @change="onTestFileChange" />
          </div>
          <button @click="uploadDataset" :disabled="!trainFile || !testFile">
            Upload Dataset & Process
          </button>
        </div>
        <div v-if="datasetResult" class="result">
          <h3>Upload Result:</h3>
          <pre>{{ datasetResult }}</pre>
        </div>
      </div>
  
      <div class="upload-section">
        <h2>View Results</h2>
        <div class="file-input">
          <button @click="viewResults">View Latest Results</button>
          <input 
            type="text" 
            v-model="resultFileName" 
            placeholder="Or enter specific file name"
          />
          <button @click="viewSpecificFile" :disabled="!resultFileName">
            View Specific File
          </button>
        </div>
        <div v-if="resultsData" class="result">
          <h3>Results:</h3>
          <pre>{{ JSON.stringify(resultsData, null, 2) }}</pre>
        </div>
        <div v-if="resultImage" class="result">
          <h3>Image:</h3>
          <img :src="resultImage" alt="Result visualization" style="max-width: 100%;" />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'FileUploader',
    data() {
      return {
        // Single file upload
        singleFile: null,
        singleFileResult: null,
        
        // Dataset upload
        trainFile: null,
        testFile: null,
        datasetResult: null,
        
        // Results
        resultFileName: '',
        resultsData: null,
        resultImage: null,
        
        // Base API URL
        apiUrl: 'http://localhost:8000/api'
      };
    },
    methods: {
      // Single file handlers
      onSingleFileChange(e) {
        this.singleFile = e.target.files[0];
      },
      async uploadSingleFile() {
        try {
          const formData = new FormData();
          formData.append('file', this.singleFile);
          
          const response = await axios.post(`${this.apiUrl}/upload/`, formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
          
          this.singleFileResult = response.data;
        } catch (error) {
          this.singleFileResult = { error: error.response?.data || error.message };
        }
      },
      
      // Dataset upload handlers
      onTrainFileChange(e) {
        this.trainFile = e.target.files[0];
      },
      onTestFileChange(e) {
        this.testFile = e.target.files[0];
      },
      async uploadDataset() {
        try {
          this.datasetResult = { status: 'Processing... This may take several minutes.' };
          
          const formData = new FormData();
          formData.append('train', this.trainFile);
          formData.append('test', this.testFile);
          
          const response = await axios.post(`${this.apiUrl}/dataset-upload/`, formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
          
          this.datasetResult = response.data;
        } catch (error) {
          this.datasetResult = { error: error.response?.data || error.message };
        }
      },
      
      // Results handlers
      async viewResults() {
        try {
          this.resultsData = { status: 'Fetching results...' };
          this.resultImage = null;
          
          const response = await axios.get(`${this.apiUrl}/results/`);
          this.resultsData = response.data;
          
          // Show first visualization if available
          if (response.data.visualization_data) {
            const images = response.data.visualization_data;
            if (Object.keys(images).length > 0) {
              this.resultImage = images[Object.keys(images)[0]];
            }
          }
        } catch (error) {
          this.resultsData = { error: error.response?.data || error.message };
        }
      },
      async viewSpecificFile() {
        try {
          this.resultsData = { status: 'Fetching file...' };
          this.resultImage = null;
          
          const response = await axios.get(`${this.apiUrl}/results/?name=${this.resultFileName}`);
          
          if (this.resultFileName.endsWith('.png') || 
              this.resultFileName.endsWith('.jpg') || 
              this.resultFileName.endsWith('.jpeg')) {
            this.resultImage = response.data.image;
            this.resultsData = null;
          } else {
            this.resultsData = response.data;
          }
        } catch (error) {
          this.resultsData = { error: error.response?.data || error.message };
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .uploader-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
  }
  
  .upload-section {
    margin-bottom: 30px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
  }
  
  .file-input {
    margin-bottom: 15px;
  }
  
  input[type="file"] {
    margin-bottom: 10px;
  }
  
  button {
    padding: 8px 16px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-right: 10px;
  }
  
  button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
  }
  
  .result {
    margin-top: 15px;
    padding: 10px;
    background-color: #f0f0f0;
    border-radius: 4px;
    overflow: auto;
  }
  
  pre {
    white-space: pre-wrap;
    word-wrap: break-word;
  }
  
  input[type="text"] {
    padding: 8px;
    width: 300px;
    margin-right: 10px;
  }
  
  h1, h2, h3 {
    color: #333;
  }
  </style>