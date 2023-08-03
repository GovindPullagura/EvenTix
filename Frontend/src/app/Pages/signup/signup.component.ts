import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/api.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css'],
})
export class SignupComponent {
  name = '';
  email = '';
  password = '';

  constructor(private apiService: ApiService, private router: Router) {}

  onSignupSubmit() {
    // Call the signup API function from the ApiService
    if (this.name == '' || this.email == '' || this.password == '') {
      alert('Fill all the details.');
    } else {
      this.apiService
        .signup(this.name, this.email, this.password)
        .then((response) => {
          console.log(response.data);
          alert(response.data.message);
          this.router.navigate(['/login']);
        })
        .catch((error) => {
          console.log('Signup error:', error);
        });
    }
  }
}
