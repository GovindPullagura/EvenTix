import { Component, OnInit } from '@angular/core';
import axios from 'axios';

@Component({
  selector: 'app-movies-page',
  templateUrl: './movies-page.component.html',
  styleUrls: ['./movies-page.component.css'],
})
export class MoviesPageComponent implements OnInit {
  movies: any[] = [];

  ngOnInit() {
    // Make API request using Axios
    axios
      .get('http://127.0.0.1:5000/movies/')
      .then((response) => {
        // Store the response data in the 'movies' array
        this.movies = response.data;
      })
      .catch((error) => {
        console.error('Error fetching movies:', error);
      });
  }
}
