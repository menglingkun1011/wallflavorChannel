package com.meng.signtest;

import android.content.Context;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.widget.Toast;

import com.meituan.android.walle.WalleChannelReader;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = MainActivity.class.getSimpleName();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        String channel = getChannelName(this);
        Log.e(TAG, "onCreate: "+channel);
        Toast.makeText(this, "渠道名字："+channel, Toast.LENGTH_SHORT).show();
    }

    /**
     * 获取渠道名字
     * @return
     */
    public static String getChannelName(Context context) {
        String channelName = "signtest_1";
        channelName= WalleChannelReader.getChannel(context);
        if(TextUtils.isEmpty(channelName)){
            channelName="signtest_1";
        }
        return channelName;
    }
}
