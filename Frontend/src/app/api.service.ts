import { Injectable } from '@angular/core';
import axios from 'axios';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private apiUrl = 'http://127.0.0.1:5000'; // Replace this with your actual API URL

  constructor() {}

  // Function to perform a POST request for login
  login(email: string, password: string) {
    const url = `${this.apiUrl}/users/login`;
    const data = {
      email: email,
      password: password,
    };
    return axios.post(url, data);
  }

  signup(name: string, email: string, password: string) {
    const url = `${this.apiUrl}/users/signup`;
    const data = {
      name: name,
      email: email,
      password: password,
    };
    return axios.post(url, data);
  }
}
