import os
import logging
from flask import Flask, render_template, request, redirect, url_for, session

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "vietnam_liberation_day")

# Routes
@app.route('/')
def index():
    # Default language is Vietnamese
    lang = session.get('lang', 'vi')
    return render_template('index.html', lang=lang)

@app.route('/history')
def history():
    lang = session.get('lang', 'vi')
    return render_template('history.html', lang=lang)

@app.route('/timeline')
def timeline():
    lang = session.get('lang', 'vi')
    return render_template('timeline.html', lang=lang)

@app.route('/gallery')
def gallery():
    lang = session.get('lang', 'vi')
    return render_template('gallery.html', lang=lang)

@app.route('/set_language/<lang>')
def set_language(lang):
    if lang in ['vi', 'en']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('index'))

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    lang = session.get('lang', 'vi')
    return render_template('404.html', lang=lang), 404

# Content dictionary for multilingual support
app.jinja_env.globals['content'] = {
    'vi': {
        'site_title': 'Ngày Giải Phóng Miền Nam Việt Nam',
        'home': 'Trang Chủ',
        'history': 'Lịch Sử',
        'timeline': 'Dòng Thời Gian',
        'gallery': 'Thư Viện Ảnh',
        'language': 'Ngôn Ngữ',
        'vietnamese': 'Tiếng Việt',
        'english': 'Tiếng Anh',
        'hero_title': 'Ngày Giải Phóng Miền Nam Việt Nam',
        'hero_subtitle': '30 Tháng 4, 1975',
        'hero_text': 'Kỷ niệm ngày thống nhất đất nước và kết thúc cuộc chiến tranh kéo dài.',
        'read_more': 'Đọc thêm',
        'overview_title': 'Tổng Quan',
        'overview_text': 'Ngày 30 tháng 4 năm 1975 đánh dấu sự kiện Quân Giải phóng Miền Nam Việt Nam tiến vào Sài Gòn, kết thúc cuộc chiến tranh Việt Nam và bắt đầu quá trình thống nhất đất nước.',
        'historical_significance': 'Ý Nghĩa Lịch Sử',
        'historical_text': 'Ngày 30/4 là ngày lễ quan trọng của Việt Nam, đánh dấu sự kết thúc của 30 năm chiến tranh và sự bắt đầu của thời kỳ hòa bình, độc lập và thống nhất.',
        'annual_celebration': 'Kỷ Niệm Hàng Năm',
        'celebration_text': 'Hàng năm, người dân Việt Nam kỷ niệm ngày này bằng các lễ hội, diễu hành, và các hoạt động khác để tưởng nhớ những hy sinh vì độc lập dân tộc.',
        'history_title': 'Lịch Sử Ngày Giải Phóng',
        'history_intro': 'Ngày 30 tháng 4 năm 1975, còn được gọi là Ngày Thống Nhất, đánh dấu sự kết thúc của cuộc chiến tranh Việt Nam và sự thống nhất của đất nước.',
        'early_history': 'Tiền Sử',
        'early_history_text': 'Sau khi Pháp rút khỏi Đông Dương năm 1954, Việt Nam bị chia cắt thành hai miền: Bắc và Nam. Điều này dẫn đến cuộc chiến tranh kéo dài hơn 20 năm.',
        'war_period': 'Thời Kỳ Chiến Tranh',
        'war_period_text': 'Từ năm 1955 đến năm 1975, cuộc chiến tranh Việt Nam đã diễn ra giữa Việt Nam Dân chủ Cộng hòa (Bắc Việt Nam) và Việt Nam Cộng hòa (Nam Việt Nam) với sự can thiệp của các cường quốc như Hoa Kỳ.',
        'ho_chi_minh_campaign': 'Chiến Dịch Hồ Chí Minh',
        'ho_chi_minh_text': 'Chiến dịch Hồ Chí Minh là chiến dịch quân sự cuối cùng của cuộc chiến tranh, bắt đầu vào ngày 26 tháng 4 và kết thúc vào ngày 30 tháng 4 năm 1975, với việc Quân Giải phóng tiến vào Sài Gòn.',
        'liberation_day': 'Ngày Giải Phóng',
        'liberation_text': 'Vào 11 giờ 30 phút ngày 30 tháng 4 năm 1975, xe tăng của Quân Giải phóng đã tiến vào Dinh Độc Lập ở Sài Gòn, kết thúc cuộc chiến tranh và mở đầu kỷ nguyên mới cho đất nước.',
        'reunification': 'Thống Nhất Đất Nước',
        'reunification_text': 'Sau ngày 30/4/1975, quá trình thống nhất đất nước chính thức bắt đầu, và đến năm 1976, nước Cộng hòa Xã hội Chủ nghĩa Việt Nam được thành lập, thống nhất hai miền Nam-Bắc.',
        'timeline_title': 'Dòng Thời Gian Lịch Sử',
        'timeline_intro': 'Khám phá các sự kiện quan trọng dẫn đến Ngày Giải Phóng 30/4/1975.',
        'gallery_title': 'Thư Viện Ảnh Lịch Sử',
        'gallery_intro': 'Bộ sưu tập hình ảnh lịch sử về Ngày Giải Phóng và các sự kiện liên quan.',
        'footer_text': '© 2023 Kỷ Niệm Ngày Giải Phóng Miền Nam Việt Nam. Tất cả các quyền được bảo lưu.'
    },
    'en': {
        'site_title': 'Vietnam Liberation Day',
        'home': 'Home',
        'history': 'History',
        'timeline': 'Timeline',
        'gallery': 'Gallery',
        'language': 'Language',
        'vietnamese': 'Vietnamese',
        'english': 'English',
        'hero_title': 'Vietnam Liberation Day',
        'hero_subtitle': 'April 30, 1975',
        'hero_text': 'Commemorating the reunification of Vietnam and the end of a long war.',
        'read_more': 'Read More',
        'overview_title': 'Overview',
        'overview_text': 'April 30, 1975 marks the event when the Liberation Army entered Saigon, ending the Vietnam War and beginning the process of national reunification.',
        'historical_significance': 'Historical Significance',
        'historical_text': 'April 30 is an important holiday in Vietnam, marking the end of 30 years of war and the beginning of a period of peace, independence, and unity.',
        'annual_celebration': 'Annual Celebration',
        'celebration_text': 'Every year, Vietnamese people commemorate this day with festivals, parades, and other activities to remember the sacrifices made for national independence.',
        'history_title': 'History of Liberation Day',
        'history_intro': 'April 30, 1975, also known as Reunification Day, marks the end of the Vietnam War and the reunification of the country.',
        'early_history': 'Early History',
        'early_history_text': 'After France withdrew from Indochina in 1954, Vietnam was divided into two regions at the 17th parallel. This led to a war that lasted more than 20 years.',
        'war_period': 'War Period',
        'war_period_text': 'From 1955 to 1975, the Vietnam War took place between the Democratic Republic of Vietnam and the Republic of Vietnam with the intervention of powers like the United States.',
        'ho_chi_minh_campaign': 'Ho Chi Minh Campaign',
        'ho_chi_minh_text': 'The Ho Chi Minh Campaign was the final military campaign of the war, beginning on April 26 and ending on April 30, 1975, with the Liberation Army entering Saigon.',
        'liberation_day': 'Liberation Day',
        'liberation_text': 'At 11:30 AM on April 30, 1975, tanks of the Liberation Army advanced into the Independence Palace in Saigon, ending the war and beginning a new era for the country.',
        'reunification': 'National Reunification',
        'reunification_text': 'After April 30, 1975, the process of national reunification officially began, and by 1976, the Socialist Republic of Vietnam was established, unifying the nation.',
        'timeline_title': 'Historical Timeline',
        'timeline_intro': 'Explore the key events leading to Liberation Day on April 30, 1975.',
        'gallery_title': 'Historical Photo Gallery',
        'gallery_intro': 'A collection of historical images about Liberation Day and related events.',
        'footer_text': '© 2023 Vietnam Liberation Day Commemoration. All rights reserved.'
    }
}

# Timeline events for multilingual support
app.jinja_env.globals['timeline_events'] = {
    'vi': [
        {
            'date': '07/05/1954',
            'title': 'Chiến thắng Điện Biên Phủ',
            'description': 'Quân đội Việt Minh đánh bại quân đội Pháp tại Điện Biên Phủ, kết thúc sự cai trị của Pháp tại Việt Nam.'
        },
        {
            'date': '21/07/1954',
            'title': 'Hiệp định Geneva',
            'description': 'Hiệp định Geneva chia Việt Nam thành hai miền tại vĩ tuyến 17, với ý định tổ chức bầu cử thống nhất vào năm 1956.'
        },
        {
            'date': '1955',
            'title': 'Hai nhà nước Việt Nam',
            'description': 'Việt Nam Dân chủ Cộng hòa và Việt Nam Cộng hòa chính thức hình thành ở hai phía của vĩ tuyến 17.'
        },
        {
            'date': '20/12/1960',
            'title': 'Thành lập Mặt trận Dân tộc Giải phóng',
            'description': 'Tổ chức này trở thành lực lượng chính trị và quân sự chính chống lại chính quyền Việt Nam Cộng hòa.'
        },
        {
            'date': '02/03/1965',
            'title': 'Hoa Kỳ bắt đầu chiến dịch ném bom',
            'description': 'Chiến dịch không kích "Rolling Thunder" của Hoa Kỳ bắt đầu nhằm vào các khu vực của Việt Nam.'
        },
        {
            'date': '30/01/1968',
            'title': 'Tổng tiến công Tết Mậu Thân',
            'description': 'Một loạt các cuộc tấn công bất ngờ của quân đội Việt Nam Dân chủ Cộng hòa và Việt Cộng vào các thành phố trên khắp Việt Nam.'
        },
        {
            'date': '27/01/1973',
            'title': 'Hiệp định Paris',
            'description': 'Hiệp định chấm dứt sự tham gia trực tiếp của Hoa Kỳ vào chiến tranh Việt Nam.'
        },
        {
            'date': '13/03/1975',
            'title': 'Chiến dịch Tây Nguyên',
            'description': 'Quân đội Giải phóng Việt Nam mở cuộc tấn công vào Tây Nguyên, bắt đầu giai đoạn cuối của chiến tranh.'
        },
        {
            'date': '26/04/1975',
            'title': 'Bắt đầu Chiến dịch Hồ Chí Minh',
            'description': 'Chiến dịch quân sự cuối cùng nhằm giải phóng Sài Gòn.'
        },
        {
            'date': '30/04/1975 - 11:30',
            'title': 'Quân Giải phóng tiến vào Dinh Độc Lập',
            'description': 'Xe tăng của Quân Giải phóng tiến vào Dinh Độc Lập, chính quyền Việt Nam Cộng hòa đầu hàng.'
        },
        {
            'date': '02/07/1976',
            'title': 'Thống nhất đất nước',
            'description': 'Việt Nam chính thức thống nhất thành Cộng hòa Xã hội Chủ nghĩa Việt Nam.'
        }
    ],
    'en': [
        {
            'date': '05/07/1954',
            'title': 'Dien Bien Phu Victory',
            'description': 'Viet Minh forces defeat French troops at Dien Bien Phu, ending French rule in Vietnam.'
        },
        {
            'date': '07/21/1954',
            'title': 'Geneva Accords',
            'description': 'The Geneva Accords divide Vietnam at the 17th parallel, with intentions to hold unification elections in 1956.'
        },
        {
            'date': '1955',
            'title': 'Two Vietnamese States',
            'description': 'The Democratic Republic of Vietnam and the Republic of Vietnam are formally established on opposite sides of the 17th parallel.'
        },
        {
            'date': '12/20/1960',
            'title': 'Formation of the National Liberation Front',
            'description': 'This organization became the main political and military force against the Republic of Vietnam government.'
        },
        {
            'date': '03/02/1965',
            'title': 'U.S. Begins Bombing Campaign',
            'description': 'Operation Rolling Thunder, a sustained U.S. bombing campaign, begins targeting areas of Vietnam.'
        },
        {
            'date': '01/30/1968',
            'title': 'Tet Offensive',
            'description': 'A series of surprise attacks by forces on cities across Vietnam.'
        },
        {
            'date': '01/27/1973',
            'title': 'Paris Peace Accords',
            'description': 'Agreement ending direct U.S. involvement in the Vietnam War.'
        },
        {
            'date': '03/13/1975',
            'title': 'Central Highlands Campaign',
            'description': 'Vietnamese liberation forces launch an offensive in the Central Highlands, beginning the final phase of the war.'
        },
        {
            'date': '04/26/1975',
            'title': 'Ho Chi Minh Campaign Begins',
            'description': 'The final military campaign to liberate Saigon.'
        },
        {
            'date': '04/30/1975 - 11:30 AM',
            'title': 'Liberation Forces Enter Independence Palace',
            'description': 'Tanks of the Liberation Army enter the Independence Palace, and the Republic of Vietnam government surrenders.'
        },
        {
            'date': '07/02/1976',
            'title': 'National Reunification',
            'description': 'Vietnam is officially reunified as the Socialist Republic of Vietnam.'
        }
    ]
}

# Gallery images
app.jinja_env.globals['gallery_images'] = [
    {
        'id': 1,
        'description_vi': 'Xe tăng tiến vào Dinh Độc Lập ngày 30/4/1975',
        'description_en': 'Tanks entering the Independence Palace on April 30, 1975',
        'source': '/static/images/tank-palace.svg'
    },
    {
        'id': 2,
        'description_vi': 'Lá cờ Giải phóng được cắm trên nóc Dinh Độc Lập',
        'description_en': 'Liberation flag raised on top of the Independence Palace',
        'source': '/static/images/flag-palace.svg'
    },
    {
        'id': 3,
        'description_vi': 'Đoàn quân Giải phóng hành quân vào Sài Gòn',
        'description_en': 'Liberation Army marching into Saigon',
        'source': '/static/images/liberation-army.svg'
    },
    {
        'id': 4,
        'description_vi': 'Người dân Sài Gòn chào đón quân Giải phóng',
        'description_en': 'Saigon residents welcoming the Liberation Army',
        'source': '/static/images/welcome-troops.svg'
    },
    {
        'id': 5,
        'description_vi': 'Tổng thống Dương Văn Minh tuyên bố đầu hàng',
        'description_en': 'President Duong Van Minh announcing surrender',
        'source': '/static/images/surrender.svg'
    },
    {
        'id': 6,
        'description_vi': 'Cuộc diễu hành mừng chiến thắng',
        'description_en': 'Victory parade celebration',
        'source': '/static/images/victory-parade.svg'
    },
    {
        'id': 7,
        'description_vi': 'Ủy ban Quân quản Sài Gòn ra mắt',
        'description_en': 'Saigon Military Management Committee inauguration',
        'source': '/static/images/military-committee.svg'
    },
    {
        'id': 8,
        'description_vi': 'Lễ mừng Thống nhất đất nước năm 1976',
        'description_en': 'Celebration of National Reunification in 1976',
        'source': '/static/images/reunification-celebration.svg'
    }
]
