import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css'],
})
export class NavbarComponent {
  isUserLoggedIn = false;
  showDropdown = false;
  user: any | null = null;

  constructor(private router: Router) {
    // Check if the user is logged in by verifying the token in local storage
    const token = localStorage.getItem('token');
    this.isUserLoggedIn = !!token;

    if (this.isUserLoggedIn) {
      const userData = localStorage.getItem('user');
      if (userData) {
        // Use a try-catch block to handle potential parsing errors
        try {
          this.user = JSON.parse(userData);
        } catch (error) {
          console.error('Error parsing user data:', error);
        }
      }
    }
  }

  // Function to toggle the dropdown menu
  toggleDropdown() {
    this.showDropdown = !this.showDropdown;
  }

  // Function to handle logout
  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');

    this.isUserLoggedIn = false;
    this.router.navigate(['/login']);
  }
}
