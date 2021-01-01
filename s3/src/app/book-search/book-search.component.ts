import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Subject } from 'rxjs';
import { debounceTime, distinctUntilChanged, switchMap } from 'rxjs/operators';

import { BookSearchService } from './book-search.service';

@Component({
  selector: 'book-search',
  templateUrl: './book-search.component.html',
  styleUrls: ['./book-search.component.scss']
})
export class BookSearchComponent {

  constructor(private bookSearchService: BookSearchService) {};

  private bookName = new Subject<string>();

  readonly bookList$ = this.bookName.pipe(
    debounceTime(300),
    distinctUntilChanged(),
    switchMap(bookName => this.bookSearchService.searchBook(bookName))
  );

  bookSearch(bookName: string) {
    this.bookName.next(bookName);
  }

}
