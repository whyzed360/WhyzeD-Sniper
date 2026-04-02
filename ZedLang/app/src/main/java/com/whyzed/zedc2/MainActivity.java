package com.whyzed.zedc2;

import android.app.Activity;
import android.os.Bundle;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.graphics.Color;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.setBackgroundColor(Color.BLACK);

        TextView tv = new TextView(this);
        tv.setText("ZeDc2: Sovereign Infrastructure Active");
        tv.setTextColor(Color.YELLOW);
        tv.setTextSize(24);

        layout.addView(tv);
        setContentView(layout);
    }
}
