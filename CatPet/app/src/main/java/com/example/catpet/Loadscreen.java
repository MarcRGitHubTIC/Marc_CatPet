package com.example.catpet;

import android.app.Dialog;
import android.content.Context;
import android.view.Window;
import android.widget.TextView;
import com.example.catpet.R;

public class Loadscreen {
    private Dialog dialog;

    public Loadscreen(Context context) {
        dialog = new Dialog(context);
        dialog.requestWindowFeature(Window.FEATURE_NO_TITLE);
        dialog.setContentView(R.layout.loadscreen);
        dialog.setCancelable(false);
    }

    public void show() {
        dialog.show();
    }

    public void dismiss() {
        dialog.dismiss();
    }

}
