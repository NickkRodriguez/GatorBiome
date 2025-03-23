<template>
    <div>
      <Bar :data="chartData" :options="chartOptions" />
    </div>
  </template>
  
  <script>
  import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale
  } from 'chart.js'
  import { Bar } from 'vue-chartjs'
  
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
  
  export default {
    name: 'MicrobiomeChart',
    components: { Bar },
    props: {
      inputData: {
        type: Object,
        required: true
      }
    },
    computed: {
      chartData() {
        return {
          labels: Object.keys(this.inputData),
          datasets: [
            {
              label: 'Microbial Abundance',
              backgroundColor: '#42a5f5',
              data: Object.values(this.inputData)
            }
          ]
        }
      },
      chartOptions() {
        return {
          responsive: true,
          plugins: {
            legend: { position: 'top' },
            title: {
              display: true,
              text: 'Microbiome Composition'
            }
          }
        }
      }
    }
  }
  </script>
  