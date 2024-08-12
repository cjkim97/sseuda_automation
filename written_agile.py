import flet as ft
import pandas as pd
from io import BytesIO, StringIO
import zipfile
import csv
from bs4 import BeautifulSoup

def main(page: ft.Page):
    page.title = "애자일썼다"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    def handle_file_picker_result(e: ft.FilePickerResultEvent):
        if e.files:
            upload_button.text = e.files[0].name
            page.update()

    file_picker = ft.FilePicker(on_result=handle_file_picker_result)
    page.overlay.append(file_picker)

    def generate_invoices(data_list):
        # 여기서 실제 데이터 처리 및 청구서 생성 로직을 구현합니다.
        # 이 예제에서는 간단한 더미 데이터를 반환합니다.
        return [
            {"번호": "001", "날짜": "2024-08-12", "금액": "100,000원"},
            {"번호": "002", "날짜": "2024-08-13", "금액": "150,000원"}
        ]

    def create_invoice_column(invoice_data):
        return ft.Column([
            ft.Text(f"청구서 번호: {invoice_data['번호']}", weight=ft.FontWeight.BOLD),
            ft.Text(f"날짜: {invoice_data['날짜']}"),
            ft.Text(f"금액: {invoice_data['금액']}"),
        ], spacing=10)

    def process_excel_file(file_bytes):
        df = pd.read_excel(BytesIO(file_bytes))
        return df.to_dict('records')

    def process_csv_file(file_bytes):
        csv_data = StringIO(file_bytes.decode('utf-8'))
        reader = csv.DictReader(csv_data)
        return list(reader)

    def process_html_file(file_bytes):
        soup = BeautifulSoup(file_bytes, 'html.parser')
        tables = soup.find_all('table')
        data = []
        for table in tables:
            headers = [th.text.strip() for th in table.find_all('th')]
            for row in table.find_all('tr')[1:]:
                row_data = [td.text.strip() for td in row.find_all('td')]
                data.append(dict(zip(headers, row_data)))
        return data

    def convert_clicked(e):
        if not upload_button.text or upload_button.text == "파일 선택":
            return

        try:
            file_bytes = file_picker.result.files[0].read()
            file_name = file_picker.result.files[0].name

            all_data = []

            if file_name.endswith('.zip'):
                with zipfile.ZipFile(BytesIO(file_bytes)) as zf:
                    for file in zf.namelist():
                        with zf.open(file) as f:
                            file_content = f.read()
                            if file.endswith('.csv'):
                                all_data.extend(process_csv_file(file_content))
                            elif file.endswith('.html') or file.endswith('.htm'):
                                all_data.extend(process_html_file(file_content))
            else:
                raise ValueError("지원하지 않는 파일 형식입니다. ZIP 파일을 업로드해주세요.")
            
            if not all_data:
                raise ValueError("처리할 수 있는 데이터가 없습니다.")

            invoices = generate_invoices(all_data)
            invoice_columns = [create_invoice_column(invoice) for invoice in invoices]
            invoices_row.controls = invoice_columns
            invoices_container.visible = True
            error_text.visible = False
            page.update()
        except Exception as ex:
            error_text.value = f"오류: {str(ex)}"
            error_text.visible = True
            invoices_container.visible = False
            page.update()

    upload_button = ft.ElevatedButton(
        "파일 선택",
        icon=ft.icons.UPLOAD_FILE,
        on_click=lambda _: file_picker.pick_files(allowed_extensions=["zip", "xlsx", "xls", "csv", "html", "htm"])
    )

    convert_button = ft.ElevatedButton("청구서작성", on_click=convert_clicked)

    invoices_row = ft.Row(spacing=20, alignment=ft.MainAxisAlignment.CENTER)
    invoices_container = ft.Container(
        content=ft.Column([
            ft.Text("생성된 청구서:", size=16, weight=ft.FontWeight.BOLD),
            invoices_row
        ]),
        visible=False
    )

    error_text = ft.Text("", color="red", visible=False)

    page.add(
        ft.Column(
            [
                ft.Text("노션에서 가저온 데이터를 ZIP 형태로 업로드해주세요.", size=20),
                ft.Row([upload_button, convert_button], alignment=ft.MainAxisAlignment.CENTER),
                error_text,
                ft.Divider(),
                invoices_container,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)