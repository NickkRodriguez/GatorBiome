import axios from "axios";

console.log("Creating API instance with baseURL: http://127.0.0.1:8000/api/");

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
});

// request interceptor for debugging
API.interceptors.request.use(
  (config) => {
    console.log("Making request to:", config.url, "with params:", config.params);
    return config;
  },
  (error) => {
    console.error("Request error:", error);
    return Promise.reject(error);
  }
);

export default API;