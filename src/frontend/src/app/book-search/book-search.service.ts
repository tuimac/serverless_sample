import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Book } from '../book';
import { Observable, throwError, of } from 'rxjs';
import { tap, map, catchError } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class BookSearchService {

  private baseurl: string = environment.baseUrl;

  constructor(private http: HttpClient) { }

  searchBooks(bookname: string): Observable<Book[]> {
    return this.http.get<Book[]>(
      `${this.baseurl}/book?name=${bookname}`
    ).pipe(
      map(data => {
        console.log(data['body']);
        return data['body'];
      }),
      catchError(error => {
        return throwError('Book not found');
      })
    );
  }
}