import { Farmbot } from "farmbot";

var SUPER_SECRET_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJ1bmtub3duIiwic3ViIjoxOTkyOSwiaWF0IjoxNjczNTMxNDQ2LCJqdGkiOiIzMTMwMzRmYS1mMWExLTQzMDktYTcxNy0zZTQyZjA3ZjkzZDMiLCJpc3MiOiIvL215LmZhcm0uYm90OjQ0MyIsImV4cCI6MTY3ODcxNTQ0NiwibXF0dCI6ImNsZXZlci1vY3RvcHVzLnJtcS5jbG91ZGFtcXAuY29tIiwiYm90IjoiZGV2aWNlXzE5OTYzIiwidmhvc3QiOiJ4aWNvbmZ1bSIsIm1xdHRfd3MiOiJ3c3M6Ly9jbGV2ZXItb2N0b3B1cy5ybXEuY2xvdWRhbXFwLmNvbTo0NDMvd3MvbXF0dCJ9.u_jBXWLmhatHfXz2yd-fWUa6IHng2ocQnuJ6ZpnA1gsKxYr1Gy5GTdFFdM6jFrSGcSrXktp2Jp_t93L2IM0461mXmpvxPViVRrbTKDEubI-g0jmLxBvOx84NDVlN-Oees0hXvOxj_ozLTY6_krYOlrs5UncqhBKDsEn9SHGojXdDek9TtwDd9mpdwieSNEe_JQa-knLigrHyk-tb0yQA1yz-jedE1bycnPNTXTa_qIHgDbMU7bO1VkhGiYcB3wbTioG3NG41oFBVP9qLBist1fu0JtNhMOERlwHQM_189Mp3OO85ilcHxpjb-i9rtMuZjZy99ca8IYEVfqhjip3p0w";
let bot = new Farmbot({ token: SUPER_SECRET_TOKEN });

bot
    .connect()
.then(function(bot){
  console.log("Bot online!");
  return bot.moveRelative({ x: 400, y: 600, z: 10, speed: 100 }); // You can chain commands.
})
.then(function(bot){
  return bot.takePhoto({});
})
.then(function(bot){
    return bot.home({speed : 100 , axis : x});
  })
.then(function(bot){
    return bot.home({speed : 100 , axis : y});
  })
.then(function(bot){
    return bot.home({speed : 100 , axis : z});
  });
   
