package empire.whyzed.aeonz;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        // This is where your AEON-Z Manifest ID lives
        String manifestID = "1b68b6235920...4f7c89e0";
        TextView status = findViewById(R.id.status);
        status.setText("Imperial ID: " + manifestID.substring(0, 16) + "...");
    }
}
