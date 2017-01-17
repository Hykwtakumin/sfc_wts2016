var Twitter = require('twitter');
var fs=require("fs");
var rl = require('readline');

var client = new Twitter({
  consumer_key: 'MjFWBvCRciIiSmroC2m2Ox1eR',
  consumer_secret: 'JwRC9Hj2OhhjPaKCwm2q5CY8hu32krIzzvXO3qgwkkv5jU7xNG',
  access_token_key: '800556259506171904-DkUFHNBdBB9oiaNd3e0ZEB2WhHmPsF5',
  access_token_secret: 'vinXJMw8C7lVKU94MYM4zHCgXnj8YeUwlTDxwPlzQKrsd'
});



//認証を行う
client.get('account/verify_credentials',
    { include_entities: false, skip_status: true },
    function (error, info, response) {
        if (error) {
            throw error;
        }
        // var myid = info.id; //wts2016team4
        // console.log('myid='+ myid);

        client.stream( 'statuses/filter', { track : '@wts2016team4' }, function( stream ) {
          // フィルターされたデータのストリームを受け取り、ツイートのテキストを表示する
          stream.on( 'data', function( tweet ) {
            var textCleaned = tweet.text.replace( /@wts2016team4/g, "" ); // アカウント名は不要
            console.log( textCleaned );

            inm_counts = 0; //出現語録集
            inm_array = [];
            is_detected = false;
            suggest_message = '';

            var inputStream = fs.createReadStream('./inm_re_lists.txt');
            var inputReadLine = rl.createInterface({'input': inputStream, 'output': {}});

            inputReadLine
                .on('line', function(line){
                  var regex =  new RegExp('' + line + '');
                  targetText = textCleaned;
                  if (regex.test(targetText) == true){
                    console.log('語録を検出しました');
                    inm_counts += 1;
                    inm_array.push(''+ regex.exec(targetText)[0] +'');
                    is_detected == true
                  }else{
                  }

                  // var spawn = require('child_process').spawn;
                  // var python_test = spawn('python', ['test.py'], {
                  //     env:{ "PYTHONIOENCODING" : "cp65001" }
                  // });
                  // var data = line;
                  //
                  // python_test.stdout.on('data', function (data) {
                  // });
                  //
                  // python_test.stdout.on('end', function (data) {
                  //   console.log(data + 'from stdout.end');
                  // });
                  //
                  // python_test.stdin.write(data);
                  // python_test.stdin.end();

                })
                .on('close', function() {
                  console.log('EOS');
                  console.log('最終的に語録は'+ inm_counts + '個検出されました');
                  console.log('検出された語録は次の通りです。'+ inm_array);

                  if (inm_counts == 0) {

                    params = {
                      status : '@' +tweet.user.screen_name + '\n淫夢語録は特に検出されませんでした。',
                      in_reply_to_status_id : tweet.id
                    }
                    client.post('statuses/update',params,function(error, tweet, response){
                      if(error) throw error;
                      console.log('tweeted!');  // Tweet body.
                      // console.log(response);  // Raw response object.
                    });
                  }else{
                    params = {
                      status : '@' + tweet.user.screen_name + '\n淫夢語録は' + inm_counts + '個検出されました。\n' +
                      '検出された語録は\n' + inm_array + '\nです。',
                      in_reply_to_status_id : tweet.id
                    }
                    client.post('statuses/update',params,function(error, tweet, response){
                      if(error) throw error;
                      console.log('tweeted!');  // Tweet body.
                      // console.log(response);  // Raw response object.
                    });
                  }

                });

          });

          stream.on('error', function (error) {
            throw error;
          });

        });
      });


        // client.stream('user', function (stream) {
        //
        //     stream.on('data', function (tweet) {
        //         var dm = tweet && tweet.direct_message;
        //         if (dm && dm.sender.id !== myid) {
        //             console.log(dm.sender.screen_name, dm.text);
        //
        //             if(dm.text == 'OK'){
        //                 client.post('direct_messages/new', {
        //                     screen_name: 'AheAhej9ueryMan',
        //                     text: '了解です。送信を承認します。'}, function(error, tweets, response){
        //                     if(error) console.log(error);
        //                     console.log('DM_ID:', tweets.id, 'sender_id', tweets.sender_id, 'recipient_id', tweets.recipient_id, 'created_at', tweets.created_at);
        //                     // socket.emit('confirm_tweet',{isConfirmed: true});
        //                     ack({confirm_result:true});
        //                 });
        //                 client.post('statuses/update', {status: data.repTW, in_reply_to_status_id: data.in_reply_to_status_id},  function(error, tweet, response) {
        //                     if(error) throw error;
        //                     console.log(tweet);  // Tweet body.
        //                     console.log(response);  // Raw response object.
        //                 });
        //                 stream.destroy();
        //             }else{
        //                 client.post('direct_messages/new', {
        //                     screen_name: 'AheAhej9ueryMan',
        //                     text: '了解です。査読結果を送信します。'}, function(error, tweets, response){
        //                     if(error) console.log(error);
        //                     console.log('DM_ID:', tweets.id, 'sender_id', tweets.sender_id, 'recipient_id', tweets.recipient_id, 'created_at', tweets.created_at);
        //                     ack({
        //                         confirm_result:false,
        //                         draft_Text: dm.text
        //                     });
        //                 });
        //                 stream.destroy();
        //             }
        //         }
        //     });
        //
        //
        //     stream.on('error', function (error) {
        //         throw error;
        //     });
        //
        // });

    // });
