# Làm rõ yêu cầu và nghiệp vụ: Hệ thống quản lý bãi đỗ xe có tích hợp AI

## 0. Vai trò và kỹ năng cần sử dụng

Bạn đóng vai **chuyên gia Phân tích nghiệp vụ (Business Analyst) và Phân tích & Thiết kế hệ thống phần mềm**, có kinh nghiệm thực tế trong việc khảo sát, mô hình hóa và đặc tả các hệ thống quản lý bãi đỗ xe.

Trong quá trình thực hiện, hãy vận dụng các phương pháp/kỹ năng phù hợp như:

* `obra/superpowers:brainstorming`: làm rõ bối cảnh, mục tiêu, phạm vi, tác nhân, quy trình và các điểm còn mơ hồ trước khi đặc tả.
* `software-requirements`: chuẩn hóa yêu cầu thành mã yêu cầu, mức ưu tiên, tiêu chí chấp nhận, giả định và câu hỏi cần làm rõ.
* Các kỹ thuật phân tích nghiệp vụ phù hợp khác nếu có, nhưng không được tự ý đưa thêm nghiệp vụ không xuất phát từ đề tài hoặc yêu cầu đã xác định.

---

# 1. Mục đích tài liệu

Tài liệu này dùng để **làm rõ yêu cầu và nghiệp vụ của hệ thống quản lý bãi đỗ xe có tích hợp AI**, làm cơ sở cho các bước tiếp theo như:

* Lập kế hoạch dự án.
* Khảo sát và phân tích nghiệp vụ.
* Xây dựng Use Case.
* Đặc tả yêu cầu phần mềm.
* Thiết kế cơ sở dữ liệu.
* Thiết kế kiến trúc và hệ thống.
* Thiết kế chức năng.
* Kiểm thử.
* Triển khai hệ thống.
* Chuẩn bị nền tảng để tích hợp các chức năng AI ở giai đoạn sau.

### Lưu ý quan trọng

**Giai đoạn hiện tại CHƯA triển khai hoặc tích hợp AI vào hệ thống.**

Không được tự ý đưa vào các chức năng như:

* Nhận dạng biển số bằng AI.
* Nhận diện khuôn mặt.
* Phát hiện phương tiện bằng Computer Vision.
* Dự đoán số lượng xe bằng Machine Learning.
* Chatbot AI.
* Sinh báo cáo bằng GenAI.
* Bất kỳ mô hình AI cụ thể nào.

Trong giai đoạn này chỉ cần **phân tích và xây dựng hệ thống quản lý bãi đỗ xe cốt lõi**, đồng thời thiết kế nghiệp vụ và dữ liệu theo hướng **có khả năng mở rộng để tích hợp AI trong tương lai**.

---

# 2. Bối cảnh nghiệp vụ

Bãi đỗ xe cần quản lý số lượng lớn phương tiện ra vào mỗi ngày. Nếu việc quản lý được thực hiện bằng sổ sách, vé giấy hoặc các file rời rạc, có thể phát sinh:

* Khó kiểm soát số lượng xe đang gửi trong bãi.
* Khó xác định vị trí xe đang đỗ.
* Mất thời gian khi xe vào và xe ra.
* Khó kiểm tra thông tin lượt gửi xe.
* Khó quản lý vé gửi xe.
* Khó tính tiền gửi xe chính xác.
* Khó quản lý nhiều loại phương tiện với mức giá khác nhau.
* Khó theo dõi doanh thu.
* Khó thống kê tình hình hoạt động của bãi xe.
* Dễ xảy ra sai lệch dữ liệu giữa số xe thực tế và dữ liệu hệ thống.
* Khó kiểm soát người dùng và quyền thực hiện nghiệp vụ.

Hệ thống cần cung cấp một nền tảng quản lý tập trung giúp nhân viên và người quản lý theo dõi toàn bộ hoạt động của bãi đỗ xe.

---

# 3. Vấn đề cần giải quyết

| Mã     | Vấn đề nghiệp vụ                                               | Hậu quả nếu không xử lý                                |
| ------ | -------------------------------------------------------------- | ------------------------------------------------------ |
| BP-001 | Thông tin xe được quản lý thủ công hoặc phân tán.              | Khó tra cứu và kiểm soát phương tiện.                  |
| BP-002 | Thông tin lượt xe vào/ra chưa được quản lý tập trung.          | Khó xác định xe đang gửi và lịch sử gửi xe.            |
| BP-003 | Số lượng vị trí đỗ và trạng thái vị trí chưa được kiểm soát.   | Khó biết bãi còn chỗ hay vị trí nào đang được sử dụng. |
| BP-004 | Giá gửi xe chưa được quản lý tập trung theo loại xe/thời gian. | Dễ tính sai phí gửi xe.                                |
| BP-005 | Thanh toán được thực hiện thủ công.                            | Khó kiểm tra lịch sử và doanh thu.                     |
| BP-006 | Dữ liệu hoạt động của bãi xe chưa được thống kê.               | Người quản lý khó đánh giá tình hình vận hành.         |
| BP-007 | Người dùng và quyền truy cập chưa được kiểm soát.              | Có nguy cơ người dùng thực hiện sai hoặc vượt quyền.   |
| BP-008 | Dữ liệu hệ thống chưa được chuẩn hóa để mở rộng.               | Khó tích hợp các chức năng AI trong tương lai.         |

---

# 4. Mục tiêu nghiệp vụ

| Mã     | Mục tiêu                                 | Cách kiểm chứng                                                                                              |
| ------ | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| BO-001 | Quản lý tập trung thông tin phương tiện. | Có thể thêm, sửa, xem, tìm kiếm và quản lý xe.                                                               |
| BO-002 | Quản lý vé và lượt gửi xe.               | Có thể ghi nhận xe vào, xe ra và tra cứu lịch sử.                                                            |
| BO-003 | Quản lý trạng thái vị trí đỗ.            | Có thể xác định vị trí đang trống hoặc đang sử dụng.                                                         |
| BO-004 | Quản lý giá gửi xe.                      | Có thể cấu hình mức giá theo loại xe và quy định của bãi.                                                    |
| BO-005 | Quản lý thanh toán.                      | Có thể ghi nhận và tra cứu các khoản thanh toán.                                                             |
| BO-006 | Hỗ trợ quản lý và thống kê.              | Có thể xem các số liệu hoạt động cơ bản của bãi xe.                                                          |
| BO-007 | Quản lý người dùng và phân quyền.        | Mỗi người dùng chỉ được thực hiện các chức năng phù hợp với quyền.                                           |
| BO-008 | Chuẩn bị nền tảng cho AI.                | Dữ liệu nghiệp vụ được tổ chức có cấu trúc, có thể sử dụng làm đầu vào cho chức năng AI trong giai đoạn sau. |

---

# 5. Phạm vi nghiệp vụ

## 5.1. Trong phạm vi

Hệ thống tập trung vào các nhóm nghiệp vụ chính:

1. **Quản lý xe.**
2. **Quản lý vé và lượt gửi xe.**
3. **Quản lý bãi đỗ và vị trí đỗ.**
4. **Quản lý giá gửi xe.**
5. **Quản lý thanh toán.**
6. **Quản lý và thống kê.**
7. **Quản lý người dùng và phân quyền.**

Các chức năng chính bao gồm:

### 5.1.1. Quản lý xe

* Xem danh sách xe.
* Thêm xe.
* Xem chi tiết xe.
* Cập nhật thông tin xe.
* Tìm kiếm xe.
* Quản lý loại xe.
* Theo dõi biển số xe.
* Theo dõi thông tin phương tiện cần thiết cho nghiệp vụ gửi xe.

### 5.1.2. Quản lý vé và lượt gửi xe

* Tạo/ghi nhận lượt xe vào.
* Ghi nhận thời gian xe vào.
* Gán vị trí đỗ cho xe.
* Quản lý vé gửi xe.
* Tra cứu lượt gửi xe.
* Ghi nhận xe ra.
* Ghi nhận thời gian xe ra.
* Tính phí gửi xe.
* Cập nhật trạng thái lượt gửi xe.
* Xem lịch sử gửi xe.

### 5.1.3. Quản lý bãi đỗ và vị trí đỗ

* Quản lý thông tin bãi đỗ.
* Quản lý khu vực đỗ xe nếu có.
* Quản lý vị trí đỗ.
* Theo dõi trạng thái vị trí.
* Xác định vị trí đang trống.
* Xác định vị trí đang có xe.
* Cập nhật trạng thái vị trí khi xe vào/ra.

### 5.1.4. Quản lý giá gửi xe

* Thêm mức giá.
* Cập nhật mức giá.
* Xem danh sách mức giá.
* Quản lý giá theo loại xe.
* Quản lý giá theo khoảng thời gian hoặc hình thức gửi nếu nghiệp vụ yêu cầu.
* Quản lý trạng thái áp dụng của mức giá.

### 5.1.5. Quản lý thanh toán

* Ghi nhận thanh toán.
* Tính số tiền phải thanh toán.
* Xác nhận trạng thái thanh toán.
* Xem lịch sử thanh toán.
* Tra cứu giao dịch theo lượt gửi xe.
* Hỗ trợ các phương thức thanh toán phù hợp với phạm vi đồ án.

### 5.1.6. Quản lý và thống kê

* Thống kê số lượng xe đang gửi.
* Thống kê số lượt xe vào/ra.
* Thống kê số vị trí đang sử dụng.
* Thống kê số vị trí còn trống.
* Thống kê doanh thu.
* Tra cứu lịch sử hoạt động.
* Lọc dữ liệu theo khoảng thời gian.
* Cung cấp các báo cáo cơ bản phục vụ người quản lý.

### 5.1.7. Quản lý người dùng và phân quyền

* Đăng nhập.
* Đăng xuất.
* Quản lý tài khoản người dùng.
* Quản lý vai trò.
* Phân quyền theo chức năng.
* Kiểm soát quyền truy cập các nghiệp vụ.
* Theo dõi người thực hiện thao tác quan trọng nếu cần.

---

# 6. Ngoài phạm vi

Trong giai đoạn hiện tại, KHÔNG triển khai:

* AI nhận dạng biển số xe.
* AI nhận diện khuôn mặt.
* AI nhận diện loại phương tiện từ hình ảnh.
* AI phát hiện xe tự động bằng camera.
* AI dự đoán tình trạng đầy/chỗ trống của bãi.
* AI dự báo lưu lượng xe.
* Chatbot AI.
* GenAI sinh báo cáo.
* Tích hợp mô hình Machine Learning/Deep Learning.
* Tích hợp camera hoặc thiết bị IoT nếu chưa có yêu cầu cụ thể.
* Tích hợp hệ thống thanh toán bên thứ ba nếu chưa được xác định.
* Tích hợp hệ thống quản lý bên ngoài.
* Các nghiệp vụ không liên quan trực tiếp đến quản lý bãi đỗ xe.

**AI chỉ được xem là định hướng mở rộng trong tương lai, không phải chức năng bắt buộc của phiên bản hiện tại.**

---

# 7. Định hướng tích hợp AI trong tương lai

Mặc dù chưa triển khai AI ở giai đoạn này, hệ thống cần được phân tích theo hướng có khả năng mở rộng.

Các dữ liệu có thể được chuẩn bị để phục vụ AI trong tương lai gồm:

* Lịch sử xe vào/ra.
* Thời gian gửi xe.
* Số lượng xe theo từng thời điểm.
* Số lượng vị trí sử dụng.
* Tỷ lệ sử dụng bãi.
* Doanh thu theo thời gian.
* Loại phương tiện.
* Lịch sử hoạt động của bãi.

Các dữ liệu này có thể là cơ sở cho những chức năng AI trong tương lai, ví dụ:

* Dự đoán lưu lượng xe.
* Dự đoán thời điểm bãi đông.
* Phân tích nhu cầu sử dụng bãi.
* Đề xuất phân bổ vị trí đỗ.
* Phát hiện các bất thường trong dữ liệu vận hành.

**Không đặc tả chi tiết các chức năng AI trên trong phiên bản yêu cầu hiện tại.**

---

# 8. Tác nhân sử dụng hệ thống

| Mã      | Tác nhân             | Mục tiêu sử dụng                                              |
| ------- | -------------------- | ------------------------------------------------------------- |
| ACT-001 | Người quản lý bãi xe | Quản lý hệ thống, người dùng và phân quyền.                   |
| ACT-001 | Người quản lý bãi xe | Theo dõi hoạt động, giá, doanh thu và thống kê.               |
| ACT-002 | Nhân viên bãi xe     | Quản lý xe vào, xe ra, vé, vị trí và thanh toán.              |

Nếu nghiệp vụ thực tế có **khách hàng/chủ phương tiện tương tác trực tiếp với hệ thống**, cần xác định rõ phạm vi tương tác trước khi đưa tác nhân này vào Use Case.

---

# 9. Quy trình nghiệp vụ tổng quan

## 9.1. Quy trình xe vào bãi

1. Xe đến cổng bãi.
2. Nhân viên ghi nhận thông tin xe.
3. Hệ thống kiểm tra thông tin phương tiện.
4. Hệ thống ghi nhận lượt gửi xe.
5. Hệ thống xác định/gán khu vực đỗ.
6. Hệ thống ghi nhận thời gian vào.
7. Hệ thống tạo thông tin vé gửi.
8. Trạng thái vị trí đỗ được cập nhật thành đang sử dụng.
9. Lượt gửi xe được chuyển sang trạng thái đang gửi.

## 9.2. Quy trình xe ra khỏi bãi

1. Xe yêu cầu ra khỏi bãi.
2. Nhân viên tra cứu lượt gửi xe/vé.
3. Hệ thống xác định thông tin lượt gửi.
4. Hệ thống xác định thời gian gửi.
5. Hệ thống tính phí.
6. Người dùng thực hiện thanh toán.
7. Hệ thống ghi nhận thanh toán.
8. Hệ thống ghi nhận thời gian xe ra.
9. Lượt gửi xe chuyển sang trạng thái đã hoàn tất.
10. Vị trí đỗ được cập nhật thành trống.

## 9.3. Quy trình quản lý khu vực đỗ

1. Người quản lý xem danh sách khu vực.
2. Hệ thống hiển thị trạng thái từng khu vực.
3. Khi xe vào, khu vực cập nhật số lượng chỗ trống.
4. Khi xe ra, khu vực cập nhật số lượng chỗ trống.
5. Người quản lý có thể tra cứu tình trạng khu vực tại từng thời điểm.

---

# 10. Quy tắc nghiệp vụ

| Mã     | Quy tắc nghiệp vụ                                                                                                | Ưu tiên |
| ------ | ---------------------------------------------------------------------------------------------------------------- | ------- |
| BR-001 | Mỗi xe phải có thông tin định danh hợp lệ theo nghiệp vụ của bãi.                                                | Must    |
| BR-002 | Biển số xe không được trùng đối với các phương tiện đang được quản lý.                                           | Must    |
| BR-003 | Mỗi lượt gửi xe phải gắn với một phương tiện hợp lệ.                                                             | Must    |
| BR-004 | Mỗi lượt gửi xe phải có thời gian vào.                                                                           | Must    |
| BR-005 | Một xe không được đồng thời có nhiều lượt gửi đang hoạt động nếu nghiệp vụ không cho phép.                       | Must    |
| BR-006 | Vị trí đang có xe không được gán cho xe khác.                                                                    | Must    |
| BR-007 | Khi xe vào, vị trí được gán phải chuyển sang trạng thái đang sử dụng.                                            | Must    |
| BR-008 | Khi xe ra hoàn tất, vị trí tương ứng phải chuyển về trạng thái trống.                                            | Must    |
| BR-009 | Phí gửi xe phải được tính dựa trên quy tắc giá đã được cấu hình.                                                 | Must    |
| BR-010 | Thanh toán phải được ghi nhận trước khi hoàn tất lượt xe ra nếu quy định của bãi yêu cầu.                        | Must    |
| BR-011 | Mỗi giao dịch thanh toán phải gắn với một lượt gửi xe hợp lệ.                                                    | Must    |
| BR-012 | Chỉ người dùng có quyền phù hợp mới được thực hiện các nghiệp vụ quản lý.                                        | Must    |
| BR-013 | Dữ liệu lượt gửi xe sau khi hoàn tất phải được lưu để phục vụ tra cứu và thống kê.                               | Must    |
| BR-014 | Dữ liệu nghiệp vụ cần được lưu trữ có cấu trúc để có thể mở rộng cho các chức năng phân tích/AI trong tương lai. | Should  |

---

# 11. Yêu cầu chức năng mức nghiệp vụ

## 11.1. Quản lý xe

| Mã             | Yêu cầu                                                      | Ưu tiên |
| -------------- | ------------------------------------------------------------ | ------- |
| FR-VEHICLE-001 | Hệ thống phải cho phép xem danh sách xe.                     | Must    |
| FR-VEHICLE-002 | Hệ thống phải cho phép thêm xe.                              | Must    |
| FR-VEHICLE-003 | Hệ thống phải cho phép cập nhật thông tin xe.                | Must    |
| FR-VEHICLE-004 | Hệ thống phải cho phép xem chi tiết xe.                      | Must    |
| FR-VEHICLE-005 | Hệ thống phải cho phép tìm kiếm xe theo thông tin định danh. | Must    |
| FR-VEHICLE-006 | Hệ thống phải quản lý loại xe.                               | Must    |

## 11.2. Quản lý vé và lượt gửi xe

| Mã             | Yêu cầu                                                 | Ưu tiên |
| -------------- | ------------------------------------------------------- | ------- |
| FR-PARKING-001 | Hệ thống phải cho phép ghi nhận xe vào bãi.             | Must    |
| FR-PARKING-002 | Hệ thống phải ghi nhận thời gian xe vào.                | Must    |
| FR-PARKING-003 | Hệ thống phải ghi nhận vị trí đỗ của xe.                | Must    |
| FR-PARKING-004 | Hệ thống phải quản lý thông tin vé/lượt gửi xe.         | Must    |
| FR-PARKING-005 | Hệ thống phải cho phép tra cứu lượt gửi đang hoạt động. | Must    |
| FR-PARKING-006 | Hệ thống phải cho phép ghi nhận xe ra.                  | Must    |
| FR-PARKING-007 | Hệ thống phải ghi nhận thời gian xe ra.                 | Must    |
| FR-PARKING-008 | Hệ thống phải tính phí gửi xe theo quy tắc giá.         | Must    |
| FR-PARKING-009 | Hệ thống phải lưu lịch sử các lượt gửi đã hoàn tất.     | Must    |

## 11.3. Quản lý khu vực đỗ

| Mã           | Yêu cầu                                             | Ưu tiên |
| ------------ | --------------------------------------------------- | ------- |
| FR-SPACE-001 | Hệ thống phải cho phép quản lý danh sách khu vực đỗ.| Must    |
| FR-SPACE-002 | Hệ thống phải hiển thị trạng thái khu vực đỗ.       | Must    |
| FR-SPACE-003 | Hệ thống phải cập nhật khu vực khi xe vào.          | Must    |
| FR-SPACE-004 | Hệ thống phải cập nhật khu vực khi xe ra.           | Must    |
| FR-SPACE-005 | Hệ thống phải cho phép kiểm tra số lượng còn trống. | Should  |

## 11.4. Quản lý giá

| Mã           | Yêu cầu                                              | Ưu tiên |
| ------------ | ---------------------------------------------------- | ------- |
| FR-PRICE-001 | Hệ thống phải cho phép xem danh sách mức giá.        | Must    |
| FR-PRICE-002 | Hệ thống phải cho phép thêm mức giá.                 | Must    |
| FR-PRICE-003 | Hệ thống phải cho phép cập nhật mức giá.             | Must    |
| FR-PRICE-004 | Hệ thống phải cho phép cấu hình giá theo loại xe.    | Must    |
| FR-PRICE-005 | Hệ thống phải xác định mức giá áp dụng khi tính phí. | Must    |

## 11.5. Thanh toán

| Mã             | Yêu cầu                                            | Ưu tiên |
| -------------- | -------------------------------------------------- | ------- |
| FR-PAYMENT-001 | Hệ thống phải tính số tiền cần thanh toán.         | Must    |
| FR-PAYMENT-002 | Hệ thống phải cho phép ghi nhận thanh toán.        | Must    |
| FR-PAYMENT-003 | Hệ thống phải quản lý trạng thái thanh toán.       | Must    |
| FR-PAYMENT-004 | Hệ thống phải cho phép tra cứu lịch sử thanh toán. | Should  |

## 11.6. Quản lý và thống kê

| Mã            | Yêu cầu                                                     | Ưu tiên |
| ------------- | ----------------------------------------------------------- | ------- |
| FR-REPORT-001 | Hệ thống phải thống kê số xe đang gửi.                      | Must    |
| FR-REPORT-002 | Hệ thống phải thống kê số lượt xe vào/ra.                   | Must    |
| FR-REPORT-003 | Hệ thống phải thống kê số lượng vị trí đang sử dụng và còn trống.| Must    |
| FR-REPORT-004 | Hệ thống phải thống kê doanh thu theo khoảng thời gian.     | Should  |
| FR-REPORT-005 | Hệ thống phải hỗ trợ tra cứu dữ liệu theo thời gian.        | Should  |

## 11.7. Người dùng và phân quyền

| Mã          | Yêu cầu                                           | Ưu tiên |
| ----------- | ------------------------------------------------- | ------- |
| FR-AUTH-001 | Hệ thống phải cho phép người dùng đăng nhập.      | Must    |
| FR-AUTH-002 | Hệ thống phải cho phép người dùng đăng xuất.      | Must    |
| FR-AUTH-003 | Hệ thống phải quản lý tài khoản người dùng.       | Must    |
| FR-AUTH-004 | Hệ thống phải quản lý vai trò người dùng.         | Must    |
| FR-AUTH-005 | Hệ thống phải kiểm soát quyền truy cập chức năng. | Must    |

---

# 12. Dữ liệu nghiệp vụ cần quản lý

Tối thiểu cần xác định các nhóm dữ liệu:

### 12.1. Xe

* Mã xe.
* Biển số xe.
* Loại xe.
* Màu xe.
* Mô tả

### 12.2. Loại xe

* Mã loại xe.
* Tên loại xe.
* Mô tả.

### 12.3. Vé gửi xe

* Mã vé.
* Loại vé
* Trạng thái vé.


### 12.4. Lượt gửi xe

* Mã lượt gửi.
* Mã vé.
* Mã xe.
* Biển số xe
* Mã khu đỗ
* Thời gian vào.
* Thời gian ra.
* Trạng thái lượt gửi.
* Số tiền phải thanh toán.
* Mã nhân viên ghi nhận xe vào
* Mã nhân viên ghi nhận xe ra
* Tổng tiền phí
* Trạng thái lượt

### 12.5. Khu vực đỗ

* Mã khu vực.
* Tên khu vực.
* Sức chứa tối đa.
* Thông tin mô tả.

### 12.6. Giá gửi xe

* Mã giá.
* Loại xe.
* Mức giá.
* Đơn vị tính thời gian
* Giá tăng thêm
* Giá ban đêm
* Ngày áp dụng.

### 12.7. Vé tháng

* Mã vé tháng.
* Mã vé.
* Loại xe.
* Họ tên khách hàng.
* Số điện thoại.
* Ngày bắt đầu.
* Ngày kết thúc.
* Trạng thái vé

### 12.8. Báo cáo thống kê

* Mã báo cáo
* Loại báo cáo
* Ngày bắt đầu
* Ngày kết thúc
* Tên khu vực
* Tổng lượt xe
* Tổng doanh thu.
* Tỷ lệ lấp đầy trung bình
* Khung giờ cao điểm
* Ngày tạo

### 12.9. Thanh toán

* Mã thanh toán.
* Mã lượt gửi.
* Số tiền.
* Thời gian thanh toán.
* Phương thức thanh toán.
* Trạng thái thanh toán.

### 12.10. Người dùng

* Mã người dùng.
* Tên đăng nhập.
* Mật khẩu
* Họ tên
* Số điện thoại
* Vai trò.
* Trạng thái.
* Thời gian tạo/cập nhật.

### 12.11. Vai trò

* Mã vai trò
* Tên vai trò
* Mô tả


### 12.8. Dữ liệu phục vụ mở rộng AI

Chưa triển khai AI nhưng cần lưu trữ có cấu trúc các dữ liệu có khả năng phục vụ phân tích trong tương lai:

* Thời gian xe vào/ra.
* Số lượng xe theo thời điểm.
* Lịch sử sử dụng vị trí.
* Loại xe.
* Thời gian gửi.
* Doanh thu.
* Tần suất sử dụng bãi.

Không tạo thêm bảng hoặc thuộc tính dành riêng cho AI nếu chưa có yêu cầu nghiệp vụ cụ thể.

---

# 13. Yêu cầu phi chức năng mức tổng quan

| Mã                  | Yêu cầu                                                                                        | Ưu tiên |
| ------------------- | ---------------------------------------------------------------------------------------------- | ------- |
| NFR-PERF-001        | Các chức năng quản lý chính phải phản hồi trong thời gian phù hợp với quy mô đồ án.            | Should  |
| NFR-SEC-001         | Thông tin xác thực và dữ liệu nhạy cảm không được hiển thị trong thông báo lỗi cho người dùng. | Must    |
| NFR-SEC-002         | Người dùng chỉ được truy cập các chức năng phù hợp với quyền.                                  | Must    |
| NFR-RELIABILITY-001 | Khi lưu dữ liệu thất bại, hệ thống phải thông báo rõ ràng và không tạo dữ liệu sai lệch.       | Must    |
| NFR-DATA-001        | Dữ liệu nghiệp vụ phải được lưu trữ nhất quán.                                                 | Must    |
| NFR-EXT-001         | Thiết kế hệ thống cần cho phép mở rộng để tích hợp chức năng AI trong các giai đoạn sau.       | Should  |
| NFR-USABILITY-001   | Các nghiệp vụ xe vào, xe ra và thanh toán phải dễ sử dụng đối với nhân viên bãi xe.            | Should  |

---

# 14. Giả định

1. Hệ thống được xây dựng phục vụ hoạt động quản lý một bãi đỗ xe hoặc mô hình bãi xe quy mô phù hợp với đồ án sinh viên.
2. Nhân viên bãi xe là người trực tiếp thực hiện các nghiệp vụ xe vào, xe ra và thanh toán.
3. Thông tin xe được nhập vào hệ thống trong giai đoạn hiện tại.
4. Chức năng AI chưa được triển khai trong phiên bản nghiệp vụ này.
5. Hệ thống được thiết kế theo hướng có khả năng mở rộng để tích hợp AI trong tương lai.
6. Cơ sở dữ liệu sử dụng `SQLite` nếu đây là ràng buộc công nghệ đã được chốt của dự án.
7. Các yêu cầu về camera, thiết bị IoT, máy quét hoặc phần cứng bên ngoài chưa được xem là bắt buộc nếu chưa có yêu cầu riêng.
8. Các quy tắc tính giá cụ thể cần được xác nhận trước khi đặc tả chi tiết.
9. Các yêu cầu về thanh toán trực tuyến cần được xác nhận trước khi triển khai.
10. Các chức năng ngoài phạm vi không được tự ý bổ sung vào hệ thống.

---

# 15. Câu hỏi cần làm rõ

| Mã    | Câu hỏi                                                              | Người phụ trách       | Trạng thái |
| ----- | -------------------------------------------------------------------- | --------------------- | ---------- |
| Q-001 | Bãi xe quản lý những loại phương tiện nào?                           | Giảng viên/nhóm dự án | Chưa chốt  |
| Q-002 | Vé gửi xe là vé giấy, vé điện tử hay chỉ là bản ghi trên hệ thống?   | Giảng viên/nhóm dự án | Chưa chốt  |
| Q-003 | Quy tắc tính giá theo giờ/ngày/đêm như thế nào?                      | Giảng viên/nhóm dự án | Chưa chốt  |
| Q-004 | Có cần quản lý vé tháng hoặc khách gửi xe dài hạn không?             | Giảng viên/nhóm dự án | Chưa chốt  |
| Q-005 | Một bãi xe có cần chia thành nhiều khu vực không?                    | Giảng viên/nhóm dự án | Chưa chốt  |
| Q-006 | Có cần quản lý xe theo vị trí đỗ cụ thể hay chỉ quản lý số lượng xe? | Giảng viên/nhóm dự án | Chưa chốt  |
| Q-007 | Có cần hỗ trợ nhiều phương thức thanh toán không?                    | Giảng viên/nhóm dự án | Chưa chốt  |
| Q-008 | Có cần quản lý doanh thu theo ca làm việc của nhân viên không?       | Giảng viên/nhóm dự án | Chưa chốt  |
| Q-009 | Có cần lưu lịch sử thao tác của người dùng không?                    | Giảng viên/nhóm dự án | Chưa chốt  |
| Q-010 | AI sẽ được tích hợp vào nghiệp vụ nào ở giai đoạn tiếp theo?         | Giảng viên/nhóm dự án | Chưa chốt  |

---

# 16. Nguyên tắc quan trọng khi thực hiện

Khi phân tích và đặc tả hệ thống:

1. Không tự ý thêm nghiệp vụ ngoài phạm vi.
2. Không tự ý tích hợp AI ở giai đoạn hiện tại.
3. Không tự ý đưa AI nhận dạng biển số vào hệ thống.
4. Không nhầm lẫn giữa **hệ thống quản lý bãi đỗ xe** và **hệ thống AI**.
5. Ưu tiên hoàn thiện nghiệp vụ quản lý bãi xe trước.
6. Các chức năng AI chỉ được xem là định hướng mở rộng.
7. Mọi yêu cầu chưa rõ phải đưa vào mục **“Câu hỏi cần làm rõ”**, không tự suy đoán.
8. Các yêu cầu đã xác nhận phải được sử dụng thống nhất trong các tài liệu tiếp theo.
9. Không tự ý thay đổi công nghệ hoặc cơ sở dữ liệu đã được nhóm dự án chốt.
10. Các tài liệu sau phải kế thừa phạm vi và yêu cầu từ tài liệu này.

---

# 17. Ghi chú chuyển tiếp

Các tài liệu tiếp theo cần kế thừa nội dung của tài liệu này:

* `01_project-plan.md`: sử dụng phạm vi nghiệp vụ để lập kế hoạch, milestone, rủi ro và deliverable.
* `02_requirements-qa.md`: tập trung giải quyết các câu hỏi chưa được xác nhận.
* `03_requirements-specification.md`: chuyển các yêu cầu đã được xác nhận thành đặc tả chính thức.
* Tài liệu Use Case: xây dựng dựa trên các tác nhân và nghiệp vụ đã xác định.
* Tài liệu thiết kế cơ sở dữ liệu: xây dựng dựa trên dữ liệu nghiệp vụ đã được xác nhận.
* Tài liệu thiết kế hệ thống: không tự ý bổ sung nghiệp vụ ngoài phạm vi.
* Tài liệu triển khai và kiểm thử: phải kiểm tra đúng các yêu cầu đã được xác nhận.

**Mục tiêu của giai đoạn này là xây dựng một hệ thống quản lý bãi đỗ xe hoàn chỉnh ở mức nghiệp vụ, có nền tảng dữ liệu và kiến trúc phù hợp để tích hợp AI ở giai đoạn sau, nhưng chưa triển khai AI.**
