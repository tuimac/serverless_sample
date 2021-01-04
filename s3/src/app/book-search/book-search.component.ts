import { Component } from '@angular/core';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';
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
  searchBooksForm: any;
  readonly bookList$;

  constructor(
    private bookSearchService: BookSearchService,
    private formBuilder: FormBuilder
  ) {
    this.searchBooksForm = this.formBuilder.group({
      bookName: ''
    });
  }

  ngOnInit() { }

  searchBooks(bookName) {
    console.log(bookName);
    this.books = this.bookSearchService.searchBooks(bookName);
    console.log(this.books);
  }
}
