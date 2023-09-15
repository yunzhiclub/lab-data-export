import {Component} from '@angular/core';
import {NzUploadXHRArgs} from 'ng-zorro-antd/upload';
import {filter, of, Subscription} from 'rxjs';
import {HttpClient, HttpResponse} from '@angular/common/http';
import * as fs from 'file-saver'

let that: AppComponent;

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'web';

  onAttachmentRemove: any;

  constructor(private httpClient: HttpClient) {
    that = this;
  }

  upload(file: NzUploadXHRArgs): Subscription {
    const formData: FormData = new FormData();
    formData.append('file', file.postFile as File);
    return that.httpClient.post(`/api/upload`,
      formData, {observe: 'events', responseType: 'arraybuffer'})
      .pipe(filter(v => v instanceof HttpResponse))
      .subscribe({
        next: data => {
          data = data as HttpResponse<ArrayBuffer>;
          const contentType = data.headers.get("content-type");
          if (contentType === 'application/zip') {
            const blob = new Blob([data.body as ArrayBuffer], {type: 'application/zip'});
            //保存
            fs.saveAs(blob, '教工三表上交数据-tute-pj.zip');
          } else {
            const blob = new Blob([data.body as ArrayBuffer], {type: 'text/plain'});
            //保存
            fs.saveAs(blob, '错误日志.txt');
          }
          return;
        }
      });
  };

  showUpdateButton() {
    return true;
  }
}
