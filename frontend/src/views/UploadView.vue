<template>
    <v-container>
      <h2>Upload Microbiome Data</h2>
      <v-file-input
        v-model="file"
        label="Choose a CSV file"
        accept=".csv"
        outlined
        dense
      />
      <v-btn @click="submit" color="primary" class="mt-4">Submit</v-btn>
      <v-alert v-if="error" type="error" class="mt-2">{{ error }}</v-alert>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        file: null,
        error: null
      }
    },
    methods: {
      async submit() {
        if (!this.file) {
          this.error = 'Please select a file first.'
          return
        }
  
        const formData = new FormData()
        formData.append('file', this.file)
  
        try {
          const res = await fetch('/api/upload/', {
            method: 'POST',
            body: formData
          })
  
          const result = await res.json()
          this.$router.push({ name: 'results', params: { data: result } })
        } catch (err) {
          this.error = 'Upload failed. Try again.'
        }
      }
    }
  }
  </script>
  