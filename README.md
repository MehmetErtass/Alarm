# Alarm
kullanıcının belirlediği bir alarm zamanı için bir alarm kurmak ve belirtilen saatte Alarm.wav dosyasını çalarak kullanıcıyı uyardıracaktır 
* datetime, time, wave ve pyaudio gibi modülleri kullanır. Kullanıcının belirlediği alarm saati ve günümüzün saati arasındaki farka bakarak alarmın çalınması gerekip gerekmediğini kontrol eder. Eğer alarm saati geçmişse, while döngüsü sonlandırılır ve program sonlanır.
* Eğer alarm saati henüz gelmediyse, time.sleep() fonksiyonu kullanılarak program her saniye bekletilir ve her döngüde tekrar kontrol edilir. Belirtilen saat geldiğinde, play_sound() fonksiyonu çağrılır ve Alarm.wav dosyası çalınmaya başlar. Dosya çalındıktan sonra, program uyku moduna alınır ve uyku süresi, dosyanın çalma süresiyle aynıdır.
