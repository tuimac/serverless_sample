import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { BookComponent } from './book/book.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'book',
    pathMatch: 'full'
  },
  {
    path: 'book',
    component: BookComponent
  }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
