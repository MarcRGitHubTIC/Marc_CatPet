package com.example.catpet;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;
public class PerfilAdapter extends RecyclerView.Adapter<PerfilAdapter.PerfilViewHolder> {

    private List<PerfilItem> items;

    public PerfilAdapter(List<PerfilItem> items) {
        this.items = items;
    }

    @NonNull
    @Override
    public PerfilViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_perfil, parent, false);
        return new PerfilViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull PerfilViewHolder holder, int position) {
        PerfilItem item = items.get(position);
        holder.texto.setText(item.getTexto());
        holder.icono.setImageResource(item.getIconoResId());
    }

    @Override
    public int getItemCount() {
        return items.size();
    }

    static class PerfilViewHolder extends RecyclerView.ViewHolder {
        TextView texto;
        ImageView icono;

        public PerfilViewHolder(@NonNull View itemView) {
            super(itemView);
            texto = itemView.findViewById(R.id.txt_info);
            icono = itemView.findViewById(R.id.img_icon);
        }
    }
}
