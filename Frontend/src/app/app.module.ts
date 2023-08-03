import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import axios from 'axios';
import { MoviesPageComponent } from './Pages/movies-page/movies-page.component';
import { LoginComponent } from './Pages/login/login.component';
import { SignupComponent } from './Pages/signup/signup.component';
import { NavbarComponent } from './Components/navbar/navbar.component';
import { MovieDetailComponent } from './Pages/movie-detail/movie-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SignupComponent,
    NavbarComponent,
    MoviesPageComponent,
    MovieDetailComponent,
  ],
  imports: [BrowserModule, AppRoutingModule, FormsModule, HttpClientModule],
  providers: [{ provide: 'AxiosInstance', useValue: axios }],
  bootstrap: [AppComponent],
})
export class AppModule {}
