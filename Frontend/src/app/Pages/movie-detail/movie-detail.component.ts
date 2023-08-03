import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import axios from 'axios';

@Component({
  selector: 'app-movie-detail',
  templateUrl: './movie-detail.component.html',
  styleUrls: ['./movie-detail.component.css'],
})
export class MovieDetailComponent implements OnInit {
  movieId!: string;
  movie: any = {}; // Initialize with an empty object

  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.movieId = params['id'];
      this.fetchMovieDetails();
    });
  }

  fetchMovieDetails(): void {
    axios
      .get(`http://127.0.0.1:5000/movies/${this.movieId}`)
      .then((response) => {
        this.movie = response.data;
      })
      .catch((error) => {
        console.error('Error fetching movie details:', error);
      });
  }
}
