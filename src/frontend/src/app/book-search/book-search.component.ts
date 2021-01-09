import { Component } from '@angular/core';
import { Book } from '../book';
import { debounceTime, distinctUntilChanged, switchMap } from 'rxjs/operators';

import { BookSearchService } from './book-search.service';
import { Observable, Subject } from 'rxjs';

@Component({
  selector: 'book-search',
  templateUrl: './book-search.component.html',
  styleUrls: ['./book-search.component.scss']
})
export class BookSearchComponent {

  booklist$: Observable<Book[]>;
  private searchBookObserver = new Subject<string>();

  constructor(private bookSearchService: BookSearchService) { }

  ngOnInit() {
    this.booklist$ = this.searchBookObserver.pipe(
      debounceTime(300),
      distinctUntilChanged(),
      switchMap((bookname: string) => this.bookSearchService.searchBooks(bookname))
    );
  }

  searchBooks(bookName: string) {
    this.searchBookObserver.next(bookName);
  }
}
