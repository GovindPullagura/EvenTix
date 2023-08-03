import { Component } from '@angular/core';
import { ApiService } from '../../api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  email = '';
  password = '';

  constructor(private apiService: ApiService, private router: Router) {}

  onLoginSubmit() {
    if (this.email == '' || this.password == '') {
      alert('Fill all the details.');
    } else {
      this.apiService
        .login(this.email, this.password)
        .then((response) => {
          // Handle the response here after successful login
          console.log('Login success:', response.data);

          // Assuming the API returns the user details and token in the response data
          const user = response.data.user;
          const token = response.data.token;

          // Store the user details and token in the local storage
          localStorage.setItem('user', JSON.stringify(user));
          localStorage.setItem('token', token);

          // Optionally, you can navigate to another component after successful login
          this.router.navigate(['/']);
        })
        .catch((error) => {
          console.log('Login error:', error);
        });
    }
  }
}
