import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { HelloWorldComponent } from './hello-world/hello-world.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule, HelloWorldComponent], 
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'] 
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
  newHobby(hobby:any){
    this.hobbies.push(hobby.value);
    hobby.value="";
    return false; 
  }
  
}


