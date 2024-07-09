import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule], // Asegúrate de incluir CommonModule aquí
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'] // Cambié `styleUrl` a `styleUrls`
})
export class AppComponent {
  title = 'my-dream-app';
  name: string;
  email: string;
  webpage: string;
  hobbies: string[];
  showHobbies: boolean;


  constructor() {
    console.log('Constructor working...');
    this.name = 'John Doe';
    this.email = 'johndoe@example.com';
    this.webpage = 'https://www.example.com';
    this.hobbies = ['futbol', 'voleyball', 'basquetball'];
    this.showHobbies = false;
  }
  toggleHobbies(){
    this.showHobbies =!this.showHobbies;
  }
  
}


