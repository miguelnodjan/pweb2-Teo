import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'my-dream-app';
  name : string;
  email;
  webpage : string;
  hobbies : string[];
  constructor(){
    console.log('Constructor working...');
    this.name = 'John Doe';
    this.email = 'johndoe@example.com';
    this.webpage = 'https://www.example.com';
    this.hobbies = ['futbol', 'voleyball', 'basquetball']
  }
  showHobbies() {
    return true;
  }
}


