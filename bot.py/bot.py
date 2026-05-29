import json,time,urllib.request
TOKEN="8494085763:AAEoc5-mOqk5ZKmhdS5SY2RDtNeyWR631Gw"
API=f"https://api.telegram.org/bot{TOKEN}/"
ADMIN_ID=7839655089
T={"start":["Привет! Я Миша.\nСервис из Москвы для всех проживающих в России.\nНаш оператор — стипендиат программы CSC, член студенческого совета МГТУ им. Баумана и волонтёр Китайского студенческого совета МГТУ им. Баумана.\n\nРежим работы: с 09:00 до 21:00 ежедневно.\n\n■ Бизнес-услуги: консультации, курсы и учебные материалы\n■ Трансграничные перевозки и поручения на покупки\n■ Аренда оборудования и бытовых вещей\n■ Услуги профессиональной печати\n■ Консультации для новых китайских студентов МГТУ им. Баумана\n\nВыберите язык / 选择语言:","你好！我是 Миша。\n本服务设于莫斯科，面向全体在俄人员提供服务。\n运营者为CSC公派留学生、莫斯科国立鲍曼技术大学本校学生会成员，同时也是莫斯科国立鲍曼技术大学中国学生会志愿者，可为本校中国新生提供全方位帮扶。\n\n服务时间：每日 09:00 — 21:00。\n\n■ 商业服务：咨询、课程、学习课件资源\n■ 跨境物流与代购服务\n■ 物品租赁服务\n■ 专业文档打印服务\n■ 鲍曼大学中国新生专属咨询\n\n选择语言 / Выберите язык:"],"help":["📖 Список команд\n\n/start — Главное меню\n/help — Список команд\n/about — Информация о сервисе\n/lang — Изменить язык\n\n💡 Можете писать свободно, я постараюсь помочь!","📖 指令列表\n\n/start — 返回主菜单\n/help — 查看指令列表\n/about — 服务简介\n/lang — 切换语言\n\n💡 也可以自由输入文字，我会尽力帮您！"],"about":["ℹ️ Информация о сервисе\n\nНаш сервис базируется в Москве.\nОператор — стипендиат CSC, член студенческого совета МГТУ им. Баумана и волонтёр Китайского студенческого совета МГТУ им. Баумана. Мы предлагаем профессиональные бизнес-услуги, трансграничные перевозки, аренду и печать документов. Все услуги отличаются доступными ценами и гарантированным качеством. Также мы предоставляем бесплатную комплексную поддержку новым китайским студентам университета.\n\nРежим работы: с 09:00 до 21:00 ежедневно。","ℹ️ 服务简介\n\n本服务位于莫斯科。\n运营者为CSC公派留学生、莫斯科国立鲍曼技术大学本校学生会成员及中国学生会志愿者。我们提供专业商业服务、跨境物流、物品租赁、文档打印，价格亲民、品质有保障，同时免费为我校中国新生提供全方位帮扶咨询。\n\n服务时间：每日 09:00 — 21:00。"],"lang_prompt":["🌐 Выберите язык / 选择语言:","🌐 选择语言 / Выберите язык:"],"lang_ok":["✅ Язык сохранён!","✅ 语言已保存！"],"menu_title":["📋 Главное меню\nРежим работы: 09:00 — 21:00","📋 主菜单\n服务时间：09:00 — 21:00"],"m2_title":["💼 Бизнес-услуги","💼 商业服务"],"m2_sub1":["💡 Профессиональные бизнес-консультации\n\nПредоставляем профессиональные бизнес-консультации по различным направлениям. Цены доступные, качество гарантировано. По деталям обращайтесь к оператору лично.\n\nРежим работы: 09:00 — 21:00","💡 商业咨询\n\n提供多领域专业商业咨询服务，价格亲民、服务有保障。详情请联系运营者私下咨询。\n\n服务时间：09:00 — 21:00"],"m2_sub2":["📚 Авторские бизнес-курсы\n\nПолноценные авторские бизнес-курсы с систематизированными знаниями, ориентированные на практику. Стоимость и содержание уточняйте у оператора。\n\nРежим работы: 09:00 — 21:00","📚 商业课程\n\n全套原创商业课程，知识体系完整、侧重实战应用。价格与课程内容可咨询运营者。\n\n服务时间：09:00 — 21:00"],"m2_sub3":["📂 Курсы и учебные материалы\n\nГотовые презентации PPT, учебные файлы и дополнительные образовательные ресурсы. Высокое качество материалов и выгодные условия сотрудничества.\n\nРежим работы: 09:00 — 21:00","📂 课件 & 课程资源\n\n成品PPT课件、学习文档及各类配套课程资源，性价比高、内容专业优质。\n\n服务时间：09:00 — 21:00"],"m3_title":["🚚 Трансграничные перевозки и поручения","🚚 跨境物流 & 代购"],"m3_common":["✈️ Доступны два вида авиадоставки: экспресс-ускоренная авиаперевозка и стандартная авиадоставка через посредников. Также предоставляется обычная наземная перевозка.\n\n🚛 Срок наземной доставки:\n• Лето, осень: около 22 дней\n• Весна, зима: около 30 дней\n\n📋 Правила компенсации:\n1. Базовая компенсация: 5 долларов США за 1 кг.\n2. Дополнительное страхование: полная компенсация при потере.\n3. Обычные товары по весу, крупногабаритные по объёму.\n4. Упаковка бесплатно.\n\n⚠️ Запрещённые грузы: горючие, взрывоопасные, оружие, сырое мясо, животные.\n\n🛒 Услуга поручения на покупки для иностранных граждан в России.\n\nТочную стоимость уточняйте у оператора。","✈️ 空运：紧急加速空运、常规人肉货代空运，同时提供普通陆运。\n\n🚛 普通陆运时效：\n• 夏季、秋季：约22天\n• 春季、冬季：约30天\n\n📋 理赔规则：\n1. 基础赔付：5美元/千克。\n2. 附加保险：货物丢失全额赔付。\n3. 常规货物按重量计费，大件按体积计费。\n4. 打包免费。\n\n⚠️ 禁运：易燃易爆品、枪械、生肉、活体动物。\n\n🛒 代购面向在俄外籍人士。\n\n具体费用请咨询运营者。"],"m3_cat1":["📦 Обычные товары","📦 普通货品"],"m3_cat2":["🧴 Жидкости","🧴 液体类货品"],"m3_cat3":["💎 Ценные предметы","💎 贵重货品"],"m3_cat4":["🛋 Крупногабаритные грузы","🛋 大件货物"],"m3_detail":["📦 Категория: {cat}\n\nДля уточнения стоимости обращайтесь к оператору.\n\nРежим работы: 09:00 — 21:00","📦 品类：{cat}\n\n具体费用请咨询运营者。\n\n服务时间：09:00 — 21:00"],"m4_title":["🔧 Аренда оборудования и бытовых вещей","🔧 物品租赁服务"],"m4_sub1":["☂️ Аренда зонтов\n\nЦены низкие. При аренде требуется залог.\n\nРежим работы: 09:00 — 21:00","☂️ 雨伞租赁\n\n价格低廉。租赁需缴纳押金。\n\n服务时间：09:00 — 21:00"],"m4_sub2":["🔋 Аренда повербанков\n\nДоступные цены, полная зарядка перед выдачей. Требуется залог。\n\nРежим работы: 09:00 — 21:00","🔋 共享充电宝租赁\n\n价格实惠，出借前均满电。需缴纳押金。\n\n服务时间：09:00 — 21:00"],"m4_sub3":["🛴 Аренда электросамокатов\n\nТехника проходит регулярное обслуживание. Требуется залог。\n\nРежим работы: 09:00 — 21:00","🛴 电动滑板车租赁\n\n设备定期检修。需缴纳押金。\n\n服务时间：09:00 — 21:00"],"m5_title":["🖨 Услуги профессиональной печати","🖨 专业文档打印服务"],"m5_sub1":["⬛ Чёрно-белая печать\n\nБыстрая работа, чёткое изображение, низкие цены.\n\nРежим работы: 09:00 — 21:00","⬛ 黑白打印\n\n出件速度快、字迹清晰，价格低廉。\n\n服务时间：09:00 — 21:00"],"m5_sub2":["🌈 Цветная печать\n\nЯркие цвета, высокое качество.\n\nРежим работы: 09:00 — 21:00","🌈 彩色打印\n\n色彩鲜亮、打印品质出色。\n\n服务时间：09:00 — 21:00"],"m1_title":["🎓 Консультации для новых китайских студентов МГТУ им. Баумана","🎓 鲍曼大学中国新生专属咨询"],"m1_sub1":["🏫 Консультация для студентов подготовительного отделения в Мытищах.\n\nОтвечаем на все вопросы. Услуга бесплатная。\n\nРежим работы: 09:00 — 21:00","🏫 梅季希校区预科生专属咨询。\n\n解答学习、住宿、证件等全部问题，免费。\n\n服务时间：09:00 — 21:00"],"m1_sub2":["🏛 Консультация для студентов основного кампуса МГТУ им. Баумана.\n\nПомогаем с учебным процессом и бытом. Услуга бесплатная。\n\nРежим работы: 09:00 — 21:00","🏛 鲍曼大学主校区正式生专属咨询。\n\n协助解答课业、生活等问题，免费。\n\n服务时间：09:00 — 21:00"],"b_m1":["🎓 Новым студентам","🎓 新生专属咨询"],"b_m2":["💼 Бизнес-услуги","💼 商业服务"],"b_m3":["🚚 Доставка & Закупки","🚚 跨境物流 & 代购"],"b_m4":["🔧 Аренда","🔧 物品租赁"],"b_m5":["🖨 Печать","🖨 文档打印"],"b_help":["❓ Помощь","❓ 帮助"],"b_lang":["🌐 Язык","🌐 语言"],"b_back":["◀️ В главное меню","◀️ 返回主菜单"]}
user_lang={}
seen_ids=set()
def gt(k,l):return T.get(k,["",""])[l]
def get_lang(c):return user_lang.get(c,0)
def kb_main(l):return{"inline_keyboard":[[{"text":gt("b_m2",l),"callback_data":"m2"},{"text":gt("b_m3",l),"callback_data":"m3"}],[{"text":gt("b_m4",l),"callback_data":"m4"},{"text":gt("b_m5",l),"callback_data":"m5"}],[{"text":gt("b_m1",l),"callback_data":"m1"}],[{"text":gt("b_help",l),"callback_data":"help"},{"text":gt("b_lang",l),"callback_data":"lang"}]]}
def kb_lang():return{"inline_keyboard":[[{"text":"🇷🇺 Русский","callback_data":"lang_0"},{"text":"🇨🇳 中文","callback_data":"lang_1"}]]}
def kb_back(l):return{"inline_keyboard":[[{"text":gt("b_back",l),"callback_data":"menu"}]]}
def kb_m1(l):return{"inline_keyboard":[[{"text":"🏫 Мытищи / 梅季希","callback_data":"m1_1"}],[{"text":"🏛 Основной кампус / 主校区","callback_data":"m1_2"}],[{"text":gt("b_back",l),"callback_data":"menu"}]]}
def kb_m2(l):return{"inline_keyboard":[[{"text":"💡 Консультации / 咨询","callback_data":"m2_1"}],[{"text":"📚 Курсы / 课程","callback_data":"m2_2"}],[{"text":"📂 Материалы / 课件","callback_data":"m2_3"}],[{"text":gt("b_back",l),"callback_data":"menu"}]]}
def kb_m3(l):return{"inline_keyboard":[[{"text":gt("m3_cat1",l),"callback_data":"m3_1"},{"text":gt("m3_cat2",l),"callback_data":"m3_2"}],[{"text":gt("m3_cat3",l),"callback_data":"m3_3"},{"text":gt("m3_cat4",l),"callback_data":"m3_4"}],[{"text":gt("b_back",l),"callback_data":"menu"}]]}
def kb_m4(l):return{"inline_keyboard":[[{"text":"☂️ Зонты / 雨伞","callback_data":"m4_1"}],[{"text":"🔋 Повербанки / 充电宝","callback_data":"m4_2"}],[{"text":"🛴 Самокаты / 滑板车","callback_data":"m4_3"}],[{"text":gt("b_back",l),"callback_data":"menu"}]]}
def kb_m5(l):return{"inline_keyboard":[[{"text":"⬛ Ч/б печать / 黑白","callback_data":"m5_1"}],[{"text":"🌈 Цветная печать / 彩色","callback_data":"m5_2"}],[{"text":gt("b_back",l),"callback_data":"menu"}]]}
def api(m,p=None):
    d=json.dumps(p).encode("utf-8")if p else None
    r=urllib.request.Request(API+m,data=d,headers={"Content-Type":"application/json"})
    try:
        with urllib.request.urlopen(r,timeout=30)as x:return json.loads(x.read().decode())
    except:return{}
def send(cid,text,mk=None):
    p={"chat_id":cid,"text":text,"parse_mode":"HTML"}
    if mk:p["reply_markup"]=mk
    api("sendMessage",p)
def edit(cid,mid,text,mk=None):
    p={"chat_id":cid,"message_id":mid,"text":text,"parse_mode":"HTML"}
    if mk:p["reply_markup"]=mk
    api("editMessageText",p)
def ans(qid):api("answerCallbackQuery",{"callback_query_id":qid})
KW_RU={"цена":"sp","цену":"sp","сколько":"sp","стоимость":"sp","дорого":"sp","дешево":"sp","прайс":"sp","доллар":"sp","логистика":"m3","доставка":"m3","перевозка":"m3","закупка":"m3","покупка":"m3","аренда":"m4","зонт":"m4","повербанк":"m4","самокат":"m4","печать":"m5","печатать":"m5","копия":"m5","курс":"m2","бизнес":"m2","консультация":"m2","ppt":"m2","презентация":"m2","студент":"m1","первокурсник":"m1","общежитие":"m1","виза":"m1","документ":"m1","контакт":"sc","связаться":"sc","оператор":"sc"}
KW_ZH={"价格":"sp","多少钱":"sp","费用":"sp","报价":"sp","物流":"m3","快递":"m3","运输":"m3","代购":"m3","租赁":"m4","租":"m4","雨伞":"m4","充电宝":"m4","滑板车":"m4","打印":"m5","复印":"m5","证件照":"m5","课程":"m2","商业":"m2","咨询":"m2","课件":"m2","ppt":"m2","新生":"m1","入学":"m1","宿舍":"m1","报到":"m1","联系":"sc","客服":"sc","人工":"sc","运营者":"sc"}
def match_kw(text,lang):
    t=text.lower()
    d=KW_RU if lang==0 else KW_ZH
    for k,v in d.items():
        if k in t:return v
    return None
def fwd(cid,u,fn,text,lang):
    ln="俄语" if lang==0 else "中文"
    tag=f"@{u}" if u else fn
    send(ADMIN_ID,f"📩 新消息\n👤 {tag}\n🆔 {cid}\n🌐 {ln}\n⏰ {time.strftime('%H:%M:%S')}\n💬 {text}")
def handle(upd):
    if"message"in upd:
        m=upd["message"];c=m["chat"]["id"];t=m.get("text","");u=m.get("from",{}).get("username","");fn=m.get("from",{}).get("first_name","");l=get_lang(c)
        print(f"[LOG]{time.strftime('%H:%M:%S')}|User:{c}|{t[:50]}")
        if t=="/start":send(c,gt("start",l),kb_lang())
        elif t=="/menu":send(c,gt("menu_title",l),kb_main(l))
        elif t=="/help":send(c,gt("help",l),kb_back(l))
        elif t=="/about":send(c,gt("about",l),kb_back(l))
        elif t=="/lang":send(c,gt("lang_prompt",l),kb_lang())
        else:
            a=match_kw(t,l)
            if a=="sp":send(c,gt("smart_price",l));fwd(c,u,fn,f"[询价]{t}",l)
            elif a=="sc":send(c,gt("smart_contact",l));fwd(c,u,fn,f"[联系]{t}",l)
            elif a=="m1":send(c,gt("m1_title",l),kb_m1(l));fwd(c,u,fn,f"[新生]{t}",l)
            elif a=="m2":send(c,gt("m2_title",l),kb_m2(l));fwd(c,u,fn,f"[商业]{t}",l)
            elif a=="m3":send(c,gt("m3_common",l)+f"\n\n{gt('m3_title',l)}",kb_m3(l));fwd(c,u,fn,f"[物流]{t}",l)
            elif a=="m4":send(c,gt("m4_title",l),kb_m4(l));fwd(c,u,fn,f"[租赁]{t}",l)
            elif a=="m5":send(c,gt("m5_title",l),kb_m5(l));fwd(c,u,fn,f"[打印]{t}",l)
            else:send(c,gt("smart_unknown",l));fwd(c,u,fn,f"[未知]{t}",l)
    elif"callback_query"in upd:
        q=upd["callback_query"];ans(q["id"]);d=q["data"];m=q["message"];c=m["chat"]["id"];mid=m["message_id"];l=get_lang(c)
        if d=="lang_0":user_lang[c]=0;send(c,gt("lang_ok",0),kb_main(0))
        elif d=="lang_1":user_lang[c]=1;send(c,gt("lang_ok",1),kb_main(1))
        elif d=="menu":edit(c,mid,gt("menu_title",l),kb_main(l))
        elif d=="m1":edit(c,mid,gt("m1_title",l),kb_m1(l))
        elif d=="m1_1":edit(c,mid,gt("m1_sub1",l),kb_back(l))
        elif d=="m1_2":edit(c,mid,gt("m1_sub2",l),kb_back(l))
        elif d=="m2":edit(c,mid,gt("m2_title",l),kb_m2(l))
        elif d=="m2_1":edit(c,mid,gt("m2_sub1",l),kb_back(l))
        elif d=="m2_2":edit(c,mid,gt("m2_sub2",l),kb_back(l))
        elif d=="m2_3":edit(c,mid,gt("m2_sub3",l),kb_back(l))
        elif d=="m3":edit(c,mid,gt("m3_common",l)+f"\n\n{gt('m3_title',l)}",kb_m3(l))
        elif d in("m3_1","m3_2","m3_3","m3_4"):
            cm={"m3_1":("m3_cat1","📦"),"m3_2":("m3_cat2","🧴"),"m3_3":("m3_cat3","💎"),"m3_4":("m3_cat4","🛋")}
            ck,e=cm[d];cn=gt(ck,l);edit(c,mid,gt("m3_detail",l).format(cat=f"{e} {cn}"),kb_back(l))
        elif d=="m4":edit(c,mid,gt("m4_title",l),kb_m4(l))
        elif d=="m4_1":edit(c,mid,gt("m4_sub1",l),kb_back(l))
        elif d=="m4_2":edit(c,mid,gt("m4_sub2",l),kb_back(l))
        elif d=="m4_3":edit(c,mid,gt("m4_sub3",l),kb_back(l))
        elif d=="m5":edit(c,mid,gt("m5_title",l),kb_m5(l))
        elif d=="m5_1":edit(c,mid,gt("m5_sub1",l),kb_back(l))
        elif d=="m5_2":edit(c,mid,gt("m5_sub2",l),kb_back(l))
        elif d=="help":edit(c,mid,gt("help",l),kb_back(l))
        elif d=="lang":edit(c,mid,gt("lang_prompt",l),kb_lang())
print("="*50);print("Миша Bot V3 - Running");print("Admin: 7839655089");print("="*50)
off=0
while True:
    try:
        r=api("getUpdates",{"offset":off,"limit":10})
        for u in r.get("result",[]):
            uid=u["update_id"];off=uid+1
            if uid not in seen_ids:seen_ids.add(uid);handle(u)
            if len(seen_ids)>500:seen_ids=set(sorted(seen_ids)[-250:])
        time.sleep(1)
    except Exception as e:print(f"Err:{e}");time.sleep(3)
