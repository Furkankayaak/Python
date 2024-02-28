# Python

Risk Altında Karar Verme Analizi Programı

Bu program, kullanıcının belirlediği doğal durumlar altında çeşitli alternatifler arasından en uygun olanını seçmeye yardımcı olur. Program, kullanıcıdan doğal durum sayısını, alternatif sayısını, her bir doğal durumun olasılığını, alternatif isimlerini ve her alternatifin her doğal durumdaki getirilerini alır. Daha sonra, bu bilgileri kullanarak fırsat kayıplarını hesaplar ve en iyi alternatifi belirler. Sonuçları kullanıcıya sunar ve en uygun alternatifi seçerken hangi faktörleri göz önünde bulundurduğunu açıklar. Bu program, risk altında karar verme süreçlerini otomatize ederek kullanıcıya zaman kazandırır ve daha bilinçli kararlar almasına yardımcı olur.



1. Kullanıcı Girişleri:
   - Kullanıcıdan doğal durum sayısı (`dogal_durum_sayisi`) ve alternatif sayısı (`alternatif_sayisi`) alınır.
   - Her doğal durum için isimler (`dogal_durumlar`) ve her alternatif için isimler (`alternatifler`) kullanıcıdan alınır.
   - Her doğal durumun olasılığı (`olasiliklar`) yüzde cinsinden kullanıcıdan alınır.

2. Olasılıkların Normalize Edilmesi:
   - Kullanıcıdan alınan olasılıklar normalize edilir. Bu, olasılıkların toplamının 1'e eşit olmasını sağlar.

3. Alternatiflerin Beklenen Değerlerinin Hesaplanması:
   - İç içe iki döngü kullanılarak her doğal durum ve her alternatif için beklenen değerler hesaplanır.
   - Her bir alternatifin beklenen değeri, o alternatifin her bir doğal durumdaki getirisinin olasılıklarla ağırlıklı ortalamasıdır.

4. En İyi Alternatifin Belirlenmesi:
   - En iyi alternatifin beklenen değeri, hesaplanan alternatif beklenen değerler arasından maksimum olan değerdir.

5. Tam Bilginin Beklenen Değeri:
   - Tam bilgi durumunda, her bir doğal durumun en iyi alternatifinin getirisi kullanılarak beklenen değer hesaplanır.

6. Fırsat Kayıplarının Hesaplanması:
   - Fırsat kayıpları, tam bilgi beklenen değeri ile her alternatifin beklenen değeri arasındaki farktır.
   - Her alternatif için fırsat kaybı hesaplanır.

7. En Düşük Fırsat Kaybına Sahip Alternatifin Seçilmesi:
   - En düşük fırsat kaybına sahip alternatif belirlenir. Bu, hangi alternatifin tam bilgi durumunda en yakın olduğunu gösterir.

8. Sonuçların Yazdırılması:
   - Program, hesaplanan beklenen değerler, tam bilgi beklenen değeri, fırsat kayıpları ve en iyi alternatifin adını ekrana yazdırır.

Bu adımların tamamlanmasının ardından program, kullanıcıya risk altında karar verme analizinin sonuçlarını sunar. Bu sonuçlar, kullanıcının verdiği girişlere ve belirlenen kriterlere dayanarak en uygun alternatifin seçilmesine yardımcı olur.


                                                                                                                                      FURKAN KAYAK
