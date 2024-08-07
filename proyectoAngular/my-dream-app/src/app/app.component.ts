import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { HelloWorldComponent } from './hello-world/hello-world.component';
import { UserComponent } from './user/user.component';
import { DataService } from './data.service';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule, HelloWorldComponent, UserComponent, HttpClient, HttpClientModule, ], 
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'] 
})
export class AppComponent {
  users = ['user1', 'user2', 'user3'];
  activated = false;
  title = 'my-dream-app';
  name: string;
  email: string;
  webpage: string;
  hobbies: string[];
  showHobbies: boolean;

  
  constructor(private dataService: DataService) {
    this.dataService.getData().subscribe((data: any[]) => {
      console.log(data)
    });
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
  sayHello(){
    alert('Hello from AppComponent!');
  }
  deleteUser(user:any){
    for(let i = 0; i < this.users.length; i++){
      if(this.users[i] === user){
        this.users.splice(i, 1);
      }
    }
  }
}


