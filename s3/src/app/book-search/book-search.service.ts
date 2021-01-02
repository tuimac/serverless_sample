import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Book } from '../book';
import { Observable, throwError } from 'rxjs';
import { tap, catchError } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class BookSearchService {

  private baseurl: string = environment.baseUrl;
  private headers = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };

  constructor(private http: HttpClient) { }

  searchBook(bookname: string): Observable<Book[]>{
    return this.http.get<Book[]>(
      `${this.baseurl}/?name=${bookname}`
    ).pipe(
      tap((data: Book[]) => {
        console.log(data);
        return data;
      }),
      catchError( error => {
        return throwError('Book not found');
      })
    );
  }
}