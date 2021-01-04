import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Subject } from 'rxjs';
import { Book } from '../book';

import { debounceTime, distinctUntilChanged, switchMap } from 'rxjs/operators';

import { BookSearchService } from './book-search.service';

@Component({
  selector: 'book-search',
  templateUrl: './book-search.component.html',
  styleUrls: ['./book-search.component.scss']
})
export class BookSearchComponent {
  books: any;
  bookgroup: any;

  constructor(
    private bookSearchService: BookSearchService,
    private formBuilder: FormBuilder
  ) {
    this.bookgroup = this.formBuilder.group({
      bookName: ''
    });
  }

  ngOnInit() { }

  searchBooks(bookName: string) {
    console.log(bookName);
    this.books = this.bookSearchService.searchBooks(bookName);
    console.log(this.books);
  }
}
