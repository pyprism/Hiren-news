# Hiren-news 

## Everything comes to an end. Recently, Facebook closed this 7 year old page with 18k followers. Useless AI.


Backend for facebook page [Hacker News](https://www.facebook.com/hn.hiren.news) .

#### Cronjob
```
#*/5 * * * * wget -O /dev/null -o /dev/null "https://domain/scrapper/"
#*/8 * * * * wget -O /dev/null -o /dev/null "https://domain/send_post/"
#0 0 */3 * * wget -O /dev/null -o /dev/null "https://domain/cleaner/"
```
