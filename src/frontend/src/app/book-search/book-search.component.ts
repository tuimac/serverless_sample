import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Book } from '../book';

import { BookSearchService } from './book-search.service';

@Component({
  selector: 'book-search',
  templateUrl: './book-search.component.html',
  styleUrls: ['./book-search.component.scss']
})
export class BookSearchComponent {
  books: any;

  constructor(private bookSearchService: BookSearchService) { }

  ngOnInit() {}

  searchBooks(bookName: string) {
    this.books = this.bookSearchService.searchBooks(bookName).subscribe();
    console.log(this.books);
  }
}
