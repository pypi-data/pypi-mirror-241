

def help():
    print("metric, studinfo, contactdet, music, sms, imagedown, swipedemo, firebase, location")

def metric(num):
    xml="""
    <?xml version="1.0" encoding="utf-8"?>
    <androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="36dp"
        android:text="Metric Converter"
        android:textColor="@android:color/holo_purple"
        android:textSize="34sp"
        android:textStyle="bold|italic"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="0.512"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <EditText
        android:id="@+id/editTextNumber"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="96dp"
        android:ems="10"
        android:inputType="number"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="0.497"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/textView" />

    <TextView
        android:id="@+id/textView2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Enter the value:"
        android:textColor="#2196F3"
        android:textSize="20sp"
        android:textStyle="bold"
        app:layout_constraintBottom_toTopOf="@+id/editTextNumber"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="0.498"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/textView"
        app:layout_constraintVertical_bias="0.428" />

    <TextView
        android:id="@+id/textView4"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginBottom="100dp"
        android:textSize="34sp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="0.498"
        app:layout_constraintStart_toStartOf="parent" />

    <TextView
        android:id="@+id/valueOfPounds"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Value is:"
        android:textColor="#F44336"
        android:textSize="20sp"
        app:layout_constraintBottom_toTopOf="@+id/textView4"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/editTextNumber"
        app:layout_constraintVertical_bias="0.924" />

    <Button
        android:id="@+id/Button12"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Inch to Centimeter"
        app:layout_constraintBottom_toTopOf="@+id/button2"
        app:layout_constraintEnd_toStartOf="@+id/button"
        app:layout_constraintHorizontal_bias="0.29"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/editTextNumber"
        app:layout_constraintVertical_bias="0.618" />

    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="72dp"
        android:layout_marginEnd="28dp"
        android:text="Kilometer to Meter"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/editTextNumber" />

    <Button
        android:id="@+id/button2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginBottom="16dp"
        android:text="Fahrenheit to Celsius"
        app:layout_constraintBottom_toTopOf="@+id/button4"
        tools:layout_editor_absoluteX="22dp"
        tools:ignore="MissingConstraints" />

    <Button
        android:id="@+id/button3"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="40dp"
        android:text="Foot to Inches"
        app:layout_constraintBottom_toTopOf="@+id/button4"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="0.582"
        app:layout_constraintStart_toEndOf="@+id/button2"
        app:layout_constraintTop_toBottomOf="@+id/button"
        app:layout_constraintVertical_bias="0.111" />

    <Button
        android:id="@+id/button4"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginBottom="48dp"
        android:text="Liter to Milliliter"
        app:layout_constraintBottom_toTopOf="@+id/valueOfPounds"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="0.507"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/editTextNumber"
        app:layout_constraintVertical_bias="1.0" />

    </androidx.constraintlayout.widget.ConstraintLayout>*/
    """
    java="""
    package com.example.kgtopound;

    import androidx.appcompat.app.AppCompatActivity;
    import android.annotation.SuppressLint;
    import android.os.Bundle;
    import android.view.View;
    import android.widget.Button;
    import android.widget.EditText;
    import android.widget.TextView;

    public class MainActivity extends AppCompatActivity {
        //Declaring Widgets
        EditText editTextNumber;
        TextView textView,textView2, textView4, valueOfPounds;
        Button Button12,Button,Button2,Button3,Button4;

        @SuppressLint("MissingInflatedId")
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);

            //Instantiating Widgets

            textView=findViewById(R.id.textView);
            textView2=findViewById(R.id.textView2);
            textView4=findViewById(R.id.textView4);
            valueOfPounds=findViewById(R.id.valueOfPounds);
            editTextNumber=findViewById(R.id.editTextNumber);
            Button12=findViewById(R.id.Button12);
            Button=findViewById(R.id.button);
            Button2=findViewById(R.id.button2);
            Button3=findViewById(R.id.button3);
            Button4=findViewById(R.id.button4);

            //Adding a click event for button (Executing the convert method when clicked)
            Button12.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                //Calling ConvertFromKiloTo Pounds Method
                    inchtocentimeter();

                }
            });
            Button.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    //Calling ConvertFromKiloTo Pounds Method
                    KilometerToMeter();

                }
            });
            Button2.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    //Calling ConvertFromKiloTo Pounds Method
                    FahrenheittoCelsius();

                }
            });
            Button3.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    //Calling ConvertFromKiloTo Pounds Method
                    foottoinches();

                }
            });
            Button4.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    //Calling ConvertFromKiloTo Pounds Method
                    litertomilliliter();

                }
            });

        }

        private void inchtocentimeter() {
            //This method will convert the  values entered in editText
            //From Kilo to pounds
            String valueEnteredinKILO=editTextNumber.getText().toString();
            //converting  string to number
            double kilo = Double.parseDouble(valueEnteredinKILO);
            //converting kilo to pounds formula
            double pounds=kilo*2.54;
            //Displaying the value resulted in textView
            textView4.setText(""+pounds);
        }
        private void KilometerToMeter() {
            //This method will convert the  values entered in editText
            //From Kilo to pounds
            String valueEnteredinKILO=editTextNumber.getText().toString();
            //converting  string to number
            double kilo = Double.parseDouble(valueEnteredinKILO);
            //converting kilo to pounds formula
            double pounds=kilo*1000;
            //Displaying the value resulted in textView
            textView4.setText(""+pounds);
        }
        private void FahrenheittoCelsius() {
            //This method will convert the  values entered in editText
            //From Kilo to pounds
            String valueEnteredinKILO=editTextNumber.getText().toString();
            //converting  string to number
            double kilo = Double.parseDouble(valueEnteredinKILO);
            //converting kilo to pounds formula
            double pounds=(kilo-32)*5/9;
            //Displaying the value resulted in textView
            textView4.setText(""+pounds);
        }
        private void foottoinches() {
            //This method will convert the  values entered in editText
            //From Kilo to pounds
            String valueEnteredinKILO=editTextNumber.getText().toString();
            //converting  string to number
            double kilo = Double.parseDouble(valueEnteredinKILO);
            //converting kilo to pounds formula
            double pounds=kilo*12;
            //Displaying the value resulted in textView
            textView4.setText(""+pounds);
        }
        private void litertomilliliter() {
            //This method will convert the  values entered in editText
            //From Kilo to pounds
            String valueEnteredinKILO=editTextNumber.getText().toString();
            //converting  string to number
            double kilo = Double.parseDouble(valueEnteredinKILO);
            //converting kilo to pounds formula
            double pounds=kilo*1000;
            //Displaying the value resulted in textView
            textView4.setText(""+pounds);
        }
        }
    """

    if(num==1):
        print(xml)
    elif(num==2):
        print(java)
    else:
        print("gandmara")

def studinfo(num):
    xml="""
    //use add class
    //activity-main.xml
    <?xml version="1.0" encoding="utf-8"?>

    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="10dp"
    >

    <TextView
        android:id="@+id/textView"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Student Information" />

    <EditText
        android:id="@+id/name"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter name of the Student:"
        android:inputType="text"
        android:minHeight="48dp"
        android:textColorHint="#2196F3" />


    <EditText
        android:id="@+id/reg"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter Register number:"
        android:inputType="number"
        android:minHeight="48dp"
        android:textColorHint="#2196F3" />

    <EditText
        android:id="@+id/dept"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter the department:"
        android:inputType="text"
        android:minHeight="48dp"
        android:textColorHint="#2196F3" />

    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Submit"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintVertical_bias="0.569" />

    </LinearLayout>
    //activity-second.xml
    <?xml version="1.0" encoding="utf-8"?>
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".Second_Page"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="10dp">

    <TextView
        android:id="@+id/result"
        android:textSize="30sp"
        android:textStyle="bold"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"/>
    </LinearLayout>
    """
    java="""
    //activity-main.java

    import androidx.appcompat.app.ActionBar;
    import androidx.appcompat.app.AppCompatActivity;
    import android.content.Intent;
    import android.os.Bundle;
    import android.view.View;
    import android.widget.Button;
    import android.widget.EditText;

    public class MainActivity extends AppCompatActivity {

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);

            /*ActionBar actionBar=getSupportActionBar();
            actionBar.setTitle("First Activity");
            getSupportActionBar().setDisplayHomeAsUpEnabled(true);
            getSupportActionBar().setHomeButtonEnabled(true);*/


            EditText Name=findViewById(R.id.name);
            EditText Reg=findViewById(R.id.reg);
            EditText Dept=findViewById(R.id.dept);

            Button button=findViewById(R.id.button);

            button.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    String nam =Name.getText().toString();
                    String re =Reg.getText().toString();
                    String dep =Dept.getText().toString();
                    Intent intent =new Intent(MainActivity.this,Second_Page.class);
                    intent.putExtra("K1",nam);
                    intent.putExtra("K2",re);
                    intent.putExtra("K3",dep);
                    startActivity(intent);
                }
            });

        }
    }
    // second-page.java

    import androidx.appcompat.app.ActionBar;
    import androidx.appcompat.app.AppCompatActivity;
    import android.content.Intent;
    import android.os.Bundle;
    import android.widget.TextView;

    public class Second_Page extends AppCompatActivity {

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_second_page);

            /*ActionBar actionBar=getSupportActionBar();
            actionBar.setTitle("Second Activity");
            getSupportActionBar().setDisplayHomeAsUpEnabled(true);
            getSupportActionBar().setHomeButtonEnabled(true);*/


            Intent intent=getIntent();

            TextView textView=findViewById(R.id.result);

            String name =intent.getStringExtra("K1");
            String reg =intent.getStringExtra("K2");
            String dept =intent.getStringExtra("K3");

            textView.setText("Name:"+name+"\nRegister no.:"+reg+"\nDepartment:"+dept);


        }
    }
    """
    if(num==1):
        print(xml)
    elif(num==2):
        print(java)
    else:
        print("gandmara")

def contactdet(num):
    xml="""
    //activity-main.xml
    <?xml version="1.0" encoding="utf-8"?>
    <androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/recyclerViewId"
        android:layout_width="409dp"
        android:layout_height="726dp"
        android:layout_marginTop="4dp"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="0.0"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        />

    </androidx.constraintlayout.widget.ConstraintLayout>    

    //contact-details.xml
    <?xml version="1.0" encoding="utf-8"?>
    <androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="wrap_content">

    <ImageView
        android:id="@+id/imageView"
        android:layout_width="100dp"
        android:layout_height="100dp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintHorizontal_bias="0.051"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintVertical_bias="1.0"
        tools:srcCompat="@tools:sample/avatars" />

    <TextView
        android:id="@+id/nameId"
        android:layout_width="265dp"
        android:layout_height="32dp"
        android:gravity="center"
        android:text="name"
        android:textSize="25sp"
        app:layout_constraintBottom_toTopOf="@+id/numberId"
        app:layout_constraintHorizontal_bias="0.534"
        app:layout_constraintStart_toEndOf="@+id/imageView"
        app:layout_constraintTop_toTopOf="@+id/imageView"
        app:layout_constraintVertical_bias="0.047" />

    <TextView
        android:id="@+id/numberId"
        android:layout_width="269dp"
        android:layout_height="30dp"
        android:gravity="center"
        android:text="number"
        android:textSize="25sp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="0.57"
        app:layout_constraintStart_toEndOf="@+id/imageView"
        app:layout_constraintTop_toBottomOf="@+id/nameId"
        app:layout_constraintVertical_bias="0.1" />
    </androidx.constraintlayout.widget.ConstraintLayout>

    """
    java="""
    //main-activiy.xml

    import androidx.appcompat.app.AppCompatActivity;
    import androidx.recyclerview.widget.LinearLayoutManager;
    import androidx.recyclerview.widget.RecyclerView;
    import android.os.Bundle;
    import java.util.Arrays;

    public class MainActivity extends AppCompatActivity {
        RecyclerView recyclerView;
        ContactAdapter contactAdapter;
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
            recyclerView=findViewById(R.id.recyclerViewId);
            contactAdapter=new ContactAdapter(
                    this,
                    Arrays.asList("Tom", "Jerry", "Mickey"),
                    Arrays.asList("123","456","789"),
                    new int[]{R.drawable.p1,R.drawable.p2,R.drawable.p3}
            );
            recyclerView.setAdapter(contactAdapter);
            recyclerView.setLayoutManager(new LinearLayoutManager(this));
        }
    }

    //contact-adapter.java
    import android.content.Context;
    import android.view.LayoutInflater;
    import android.view.View;
    import android.view.ViewGroup;
    import androidx.annotation.NonNull;
    import androidx.recyclerview.widget.RecyclerView;
    import java.util.List;

    public class ContactAdapter  extends RecyclerView.Adapter<ContactViewHolder> {
        List<String> nameList;
        List<String> numberList;
        LayoutInflater layoutInflater;
        int images[];
        ContactAdapter(Context context,List<String> nameList,List<String> numberList,int images[]){
            this.nameList=nameList;
            this.numberList=numberList;
            this.images=images;
            layoutInflater=LayoutInflater.from(context);
        }
        @NonNull
        @Override
        public ContactViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType){
            View view=layoutInflater.inflate(R.layout.contact_details,parent, false);
            return new ContactViewHolder(view,numberList);
        }
        @Override
        public void onBindViewHolder(@NonNull ContactViewHolder holder,int position){
            holder.nameTextView.setText(nameList.get(position));
            holder.numberTextView.setText(numberList.get(position));
            holder.imageView.setImageResource(images[position]);
        }
        public int getItemCount(){return nameList.size();}
    }

    //contactviewholder.java

    import android.content.Context;
    import android.content.Intent;
    import android.net.Uri;
    import android.view.View;
    import android.widget.ImageView;
    import android.widget.TextView;
    import androidx.annotation.NonNull;
    import androidx.recyclerview.widget.RecyclerView;
    import java.util.List;

    public class ContactViewHolder extends RecyclerView.ViewHolder implements View.OnClickListener {
        public ImageView imageView;
        public TextView nameTextView,numberTextView;
        List<String> numberList;
        public ContactViewHolder(@NonNull View itemView, List<String> numberList){
            super(itemView);
            itemView.setOnClickListener(this);
            imageView=itemView.findViewById(R.id.imageView);
            nameTextView=itemView.findViewById(R.id.nameId);
            numberTextView=itemView.findViewById(R.id.numberId);
            this.numberList=numberList;
        }
        @Override
        public void onClick(View view){
            int position=getLayoutPosition();
            String element=numberList.get(position);
            Context context=view.getContext();
            context.startActivity(new Intent(Intent.ACTION_DIAL, Uri.parse("tel:"+element)));
        }
    }


    """
    if(num==1):
        print(xml)
    elif(num==2):
        print(java)
    else:
        print("gandmaara")

def music(num):
    xml="""
    <?xml version="1.0" encoding="utf-8"?>
    <RelativeLayout
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:context=".MainActivity">

        <TextView
            android:id="@+id/txtVw1"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Now Playing: "
            android:layout_marginTop="30dp"
            android:textAppearance="?android:attr/textAppearance"
            />
        <TextView
            android:id="@+id/txtSname"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_alignBaseline="@+id/txtVw1"
            android:layout_toRightOf="@+id/txtVw1"
            android:text="TextView"
            />
        <ImageButton
            android:id="@+id/btnBackward"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_alignParentBottom="true"
            android:layout_marginTop="44dp"
            android:layout_marginLeft="20dp"
            android:src="@android:drawable/ic_media_rew"
            />

        <ImageButton
            android:id="@+id/btnPlay"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_alignTop="@+id/btnBackward"
            android:layout_marginLeft="20dp"
            android:layout_toRightOf="@+id/btnBackward"
            android:src="@android:drawable/ic_media_play" />

        <ImageButton
            android:id="@+id/btnPause"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_alignTop="@+id/btnPlay"
            android:layout_marginLeft="20dp"
            android:layout_toRightOf="@+id/btnPlay"
            android:src="@android:drawable/ic_media_pause" />

        <ImageButton
            android:id="@+id/btnForward"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_alignTop="@+id/btnPause"
            android:layout_marginLeft="20dp"
            android:layout_toRightOf="@+id/btnPause"
            android:src="@android:drawable/ic_media_ff" />

        <TextView
            android:id="@+id/txtStartTime"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_alignTop="@+id/sBar"
            android:text="0 min, 0 sec"
            />

        <SeekBar
            android:id="@+id/sBar"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_above="@+id/btnBackward"
            android:layout_toLeftOf="@+id/txtSongTime"
            android:layout_toRightOf="@+id/txtStartTime" />

        <TextView
            android:id="@+id/txtSongTime"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_toRightOf="@+id/btnForward"
            android:layout_alignTop="@+id/sBar"
            android:text="0 min, 0 sec "
            />

    </RelativeLayout>
    """
    java="""
    import androidx.appcompat.app.AppCompatActivity;

    import android.media.MediaPlayer;
    import android.os.Bundle;
    import android.os.Handler;
    import android.provider.ContactsContract;
    import android.view.View;
    import android.widget.ImageButton;
    import android.widget.SeekBar;
    import android.widget.TextView;
    import android.widget.Toast;

    import java.util.concurrent.TimeUnit;

    public class MainActivity extends AppCompatActivity {

        private ImageButton forwardbtn, backwardbtn, pausebtn, playbtn;
        private MediaPlayer mPlayer;
        private TextView songName, startTime, songTime;
        private SeekBar songPrgs;
        private static int oTime=0,sTime=0,eTime=0,fTime=5000,bTime=5000;
        private Handler hdlr=new Handler();
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
            backwardbtn=(ImageButton)findViewById(R.id.btnBackward);
            forwardbtn=(ImageButton)findViewById(R.id.btnForward);
            playbtn=(ImageButton)findViewById(R.id.btnPlay);
            pausebtn=(ImageButton)findViewById(R.id.btnPause);
            songName=(TextView)findViewById(R.id.txtSname);
            startTime=(TextView)findViewById(R.id.txtStartTime);
            songTime=(TextView)findViewById(R.id.txtSongTime);
            songName.setText("sng.mp3");
            mPlayer=MediaPlayer.create(this,R.raw.sng);
            songPrgs=(SeekBar)findViewById(R.id.sBar);
            songPrgs.setClickable(false);
            songPrgs.setEnabled(false);
            playbtn.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    Toast.makeText(MainActivity.this,"Playing Audio!",Toast.LENGTH_SHORT).show();
                    mPlayer.start();
                    eTime=mPlayer.getDuration();
                    sTime=mPlayer.getCurrentPosition();
                    if(oTime==0){
                        songPrgs.setMax(eTime);
                        oTime=1;
                    }
                    songTime.setText(String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(eTime),
                            TimeUnit.MILLISECONDS.toSeconds(eTime)-TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(eTime))));
                    startTime.setText(String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(sTime),
                            TimeUnit.MILLISECONDS.toSeconds(sTime)-TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(sTime))));
                    songPrgs.setProgress(sTime);
                    hdlr.postDelayed(UpdateSongTime,100);
                    pausebtn.setEnabled(true);
                    playbtn.setEnabled(false);
                }
            });
            pausebtn.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    mPlayer.pause();
                    pausebtn.setEnabled(false);
                    playbtn.setEnabled(true);
                    Toast.makeText(getApplicationContext(),"Pausing Audio!",Toast.LENGTH_SHORT).show();
                }
            });
            forwardbtn.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if((sTime+fTime)<=eTime)
                    {
                        sTime=sTime+fTime;
                        mPlayer.seekTo(sTime);
                    }
                    else
                    {
                    Toast.makeText(getApplicationContext(),"Cannot jump forward 5 seconds!",Toast.LENGTH_SHORT).show();
                    }
                    if(!playbtn.isEnabled()){
                        playbtn.setEnabled(true);
                    }
                }
            });
            backwardbtn.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if((sTime-bTime)>0)
                    {
                        sTime=sTime-bTime;
                        mPlayer.seekTo(sTime);
                    }
                    else
                    {
                        Toast.makeText(getApplicationContext(),"Cannot jump backward 5 seconds!",Toast.LENGTH_SHORT).show();
                    }
                    if(!playbtn.isEnabled()){
                        playbtn.setEnabled(true);
                    }
                }
            });
        }
        private Runnable UpdateSongTime=new Runnable() {
            @Override
            public void run() {
                sTime=mPlayer.getCurrentPosition();
                startTime.setText(String.format("%d min,%d sec", TimeUnit.MILLISECONDS.toMinutes(sTime),
                        TimeUnit.MILLISECONDS.toSeconds(sTime)-TimeUnit.MINUTES.toSeconds(TimeUnit.MILLISECONDS.toMinutes(sTime))));
                songPrgs.setProgress(sTime);
                hdlr.postDelayed(this,100);
          }
        };
    }
    """
    if(num==1):
        print(xml)
    elif(num==2):
        print(java)
    else:
        print("gandmaara")

def sms(num):

    xml="""
    <?xml version="1.0" encoding="utf-8"?>
    <RelativeLayout
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:paddingBottom="16dp"
        android:paddingLeft="16dp"
        android:paddingRight="16dp"
        android:paddingTop="16dp"
        tools:context=".MainActivity">

        <TextView
            android:id="@+id/txtVw1"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="ComposeTo: "
            android:layout_marginTop="30dp"
            android:textAppearance="?android:attr/textAppearanceMedium"
            />
        <EditText
            android:id="@+id/Cname"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_alignBaseline="@+id/txtVw1"
            android:layout_marginLeft="10dp"
            android:layout_toRightOf="@+id/txtVw1"
            android:hint="Contact Number"
            />

        <ImageButton
            android:id="@+id/contactbook"
            android:layout_width="49dp"
            android:layout_height="54dp"
            android:layout_marginLeft="10dp"
            android:layout_marginTop="25dp"
            android:layout_toRightOf="@+id/Cname"
            android:src="@drawable/ic_baseline_import_contacts_24" />
        <EditText
            android:id="@+id/sms"
            android:layout_width="300dp"
            android:layout_height="wrap_content"
            android:layout_alignParentBottom="true"
            android:layout_alignBottom="@+id/txtVw1"
            android:layout_marginLeft="20dp"
            />

        <ImageButton
            android:id="@+id/send"
            android:layout_width="wrap_content"
            android:layout_height="56dp"
            android:layout_alignTop="@+id/sms"
            android:layout_marginLeft="20dp"
            android:layout_marginTop="0dp"
            android:layout_toRightOf="@+id/sms"
            android:src="@drawable/ic_baseline_send_24" />

    </RelativeLayout>
    """
    java="""
    import androidx.annotation.NonNull;
    import androidx.appcompat.app.AppCompatActivity;
    import androidx.core.app.ActivityCompat;
    import androidx.core.content.ContextCompat;

    import android.app.Activity;
    import android.content.Intent;
    import android.content.pm.PackageManager;
    import android.database.Cursor;
    import android.net.Uri;
    import android.os.Bundle;
    import android.provider.ContactsContract;
    import android.telephony.SmsManager;
    import android.view.View;
    import android.widget.EditText;
    import android.widget.ImageButton;
    import android.widget.TextView;
    import android.widget.Toast;
    import android.Manifest;


    public class MainActivity extends AppCompatActivity {

        EditText msg_send;
        EditText cn;
        TextView tv;
        ImageButton open, send_msg;
        private static final int CONTACT_PERMISSION_CODE=1;
        private static final int CONTACT_PICK_CODE=2;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
            cn=findViewById(R.id.Cname);
            msg_send=findViewById(R.id.sms);
            send_msg=findViewById(R.id.send);
            tv=findViewById(R.id.sms);
            open=findViewById(R.id.contactbook);
            open.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if(checkContactPermission()){
                        pickContactIntent();
                    }
                    else{
                        requestContactPermission();
                    }
                }
            });
            send_msg.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if (ContextCompat.checkSelfPermission(MainActivity.this,Manifest.permission.SEND_SMS)== PackageManager.PERMISSION_GRANTED){
                        sendMessage();
                    }
                    else{
                        ActivityCompat.requestPermissions(MainActivity.this,new String[]{Manifest.permission.SEND_SMS},100);
                    }
                }
            });
        }
        private void sendMessage(){
            String phoneno=cn.getText().toString().trim();
            String message=msg_send.getText().toString().trim();
            if(!phoneno.equals("") && !message.equals("")){
                SmsManager smsManager = SmsManager.getDefault();
                smsManager.sendTextMessage(phoneno,null,message,null,null);
                Toast.makeText(this, "SMS SENT SUCESSFULLY!", Toast.LENGTH_SHORT).show();
            }else{
                Toast.makeText(this, "Type some message!", Toast.LENGTH_SHORT).show();
            }
        }
        private boolean checkContactPermission(){
            boolean result=ContextCompat.checkSelfPermission(this,
                    Manifest.permission.READ_CONTACTS)==(PackageManager.PERMISSION_GRANTED);
            return result;
        }
        private void requestContactPermission(){
            String[] permissions={Manifest.permission.READ_CONTACTS};
            ActivityCompat.requestPermissions(this,permissions,CONTACT_PERMISSION_CODE);
        }
        private void pickContactIntent(){
            Intent intent = new Intent(Intent.ACTION_PICK, ContactsContract.CommonDataKinds.Phone.CONTENT_URI);
            startActivityForResult(intent,CONTACT_PICK_CODE);
        }

        @Override
        public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions,@NonNull int[] grantResults){
            super.onRequestPermissionsResult(requestCode,permissions,grantResults);
            if(requestCode==CONTACT_PERMISSION_CODE){
                if(grantResults.length>0 && grantResults[0]==PackageManager.PERMISSION_GRANTED){
                    pickContactIntent();
                }
                else{
                    Toast.makeText(this,"Permission Denied",Toast.LENGTH_SHORT).show();
                }
            }
            if(requestCode==100 && grantResults.length>0 && grantResults[0]==PackageManager.PERMISSION_GRANTED){
                sendMessage();
            }else{
                Toast.makeText(this,"Permission Denied",Toast.LENGTH_SHORT).show();
            }
        }
        @Override
        protected void onActivityResult(int requestCode,int resultCode,@NonNull Intent data){
            super.onActivityResult(requestCode,resultCode,data);
            if(requestCode==RESULT_OK){
                switch (requestCode){
                    case CONTACT_PICK_CODE:
                        contactPicked (data);
                        break;
                }
            }
            else{
                Toast.makeText(this ,"Failed to Pick Contact",Toast.LENGTH_SHORT).show();
            }
        }
        private void contactPicked(Intent data){
            Cursor cursor=null;
            try{
                String phoneNo =null;
                Uri uri =data.getData();
                cursor= getContentResolver().query(uri,null,null,null,null);
                cursor.moveToFirst();
                int phoneIndex=cursor.getColumnIndex(ContactsContract.CommonDataKinds.Phone.NUMBER);
                phoneNo=cursor.getString(phoneIndex);
                cn.setText(phoneNo);
            }catch (Exception e){
                e.printStackTrace();
           }
        }
    }
    """
    if(num==1):
        print(xml)
    elif(num==2):
        print(java)
    else:
        print("gandmara")

def imagedown(num):

    xml="""
    <?xml version="1.0" encoding="utf-8"?>
    <RelativeLayout
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:context=".MainActivity">

    <Button
        android:id="@+id/button2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentEnd="true"
        android:layout_alignParentBottom="true"
        android:layout_marginEnd="144dp"
        android:layout_marginBottom="547dp"
        android:gravity="center"
        android:text="Download"
        tools:layout_editor_absoluteX="158dp"
        tools:layout_editor_absoluteY="82dp"
        />

        <ImageView
            android:id="@+id/imageView"
            android:layout_width="383dp"
            android:layout_height="479dp"
            android:layout_alignParentBottom="true"
            android:layout_alignParentEnd="true"
            android:layout_marginBottom="41dp"
            android:layout_marginEnd="9dp"
            tools:srcCompat="@tools:sample/backgrounds/scenic"
            android:src="@drawable/bailey"
            />

    </RelativeLayout>
    """
    java="""
    import  androidx.appcompat.app.AppCompatActivity;

    import android.app.ProgressDialog;
    import android.graphics.Bitmap;
    import android.graphics.BitmapFactory;
    import android.os.AsyncTask;
    import android.os.Bundle;
    import android.view.View;
    import android.widget.Button;
    import android.widget.ImageView;

    import java.io.IOException;
    import java.io.InputStream;
    import java.net.HttpURLConnection;
    import java.net.URL;

    public class MainActivity extends AppCompatActivity {
        URL ImageUrl =null;
        InputStream is = null;
        Bitmap bmImg=null;
        ImageView image;
        ProgressDialog p;
        Button download;
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);

            download = findViewById(R.id.button2);
            image=findViewById(R.id.imageView);
            download.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    AsyncTaskExample asyncTask=new AsyncTaskExample();
                    asyncTask.execute("https://karunya.edu/sites/default/files/img/images/37,P20Years,P20KITS,P203.jpg.pagespeed.ce.CT73xojF3W.jpg");
                }
            });
        }
        private class AsyncTaskExample extends AsyncTask<String,String,Bitmap>{
            @Override
                    protected void onPreExecute(){
                super.onPreExecute();
                p=new ProgressDialog(MainActivity.this);
                p.setMessage("Please wait.... It is downloading");
                p.setIndeterminate(false);
                p.setCancelable(false);
                p.show();
            }
            @Override
            protected Bitmap doInBackground(String... strings){
                try{
                    ImageUrl = new URL(strings[0]);
                    HttpURLConnection conn =(HttpURLConnection) ImageUrl.openConnection();
                    conn.setDoInput(true);
                    conn.connect();
                    is=conn.getInputStream();
                    BitmapFactory.Options options=new BitmapFactory.Options();
                    options.inPreferredConfig=Bitmap.Config.RGB_565;
                    bmImg=BitmapFactory.decodeStream(is,null,options);
                }
                catch (IOException e){
                    e.printStackTrace();
                }
                return bmImg;
            }
            @Override
            protected void onPostExecute(Bitmap bitmap){
                super.onPostExecute(bitmap);
                if(image!=null){
                    p.hide();
                    image.setImageBitmap(bitmap);
                }else {
                    p.show();
                }
           }
        }
    }
    """
    if(num==1):
        print(xml)
    elif(num==2):
        print(java)
    else:
        print("gandmara")

def swipedemo(num):

    xml="""
    //main-activity.xml
    <?xml version="1.0" encoding="utf-8"?>
    <androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:context=".MainActivity">

        <com.google.android.material.tabs.TabLayout
            android:id="@+id/tabLayout"
            android:layout_width="409dp"
            android:layout_height="wrap_content"
            android:layout_marginStart="1dp"
            android:layout_marginEnd="1dp"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toTopOf="parent" />

        <androidx.viewpager2.widget.ViewPager2
            android:id="@+id/viewPagerId"
            android:layout_width="409dp"
            android:layout_height="681dp"
            android:layout_marginStart="1dp"
            android:layout_marginTop="1dp"
            android:layout_marginEnd="1dp"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/tabLayout" />

    </androidx.constraintlayout.widget.ConstraintLayout>

    //fragment1.xml
    <?xml version="1.0" encoding="utf-8"?>
    <FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:context=".FirstFragment">

        <!-- TODO: Update blank fragment layout -->
        <TextView
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:text="First Fragment" />

    </FrameLayout>

    //fragment2.xml
    <?xml version="1.0" encoding="utf-8"?>
    <FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:context=".SecondFragment">

        <!-- TODO: Update blank fragment layout -->
        <TextView
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:text="Second Fragment" />

    </FrameLayout>

    //fragment3.xml
    <?xml version="1.0" encoding="utf-8"?>
    <androidx.constraintlayout.widget.ConstraintLayout
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:id="@+id/frameLayout"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:context=".ThirdFragment">

        <!-- TODO: Update blank fragment layout -->


        <androidx.recyclerview.widget.RecyclerView
            android:id="@+id/recyclerView"
            android:layout_width="409dp"
            android:layout_height="729dp"
            android:layout_marginStart="1dp"
            android:layout_marginTop="1dp"
            android:layout_marginEnd="1dp"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toTopOf="parent" />
    </androidx.constraintlayout.widget.ConstraintLayout>
    """
    java="""
    //main-activity.java
    import androidx.annotation.NonNull;
    import androidx.appcompat.app.AppCompatActivity;
    import androidx.fragment.app.Fragment;
    import androidx.viewpager2.widget.ViewPager2;

    import android.os.Bundle;

    import com.google.android.material.tabs.TabLayout;
    import com.google.android.material.tabs.TabLayoutMediator;

    import java.util.ArrayList;

    public class MainActivity extends AppCompatActivity implements TabLayoutMediator.TabConfigurationStrategy {

        ViewPager2 viewPager2;
        TabLayout tabLayout;
        ArrayList<String> tabTitles;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
            viewPager2 = findViewById(R.id.viewPagerId);
            tabLayout = findViewById(R.id.tabLayout);
            ViewPager2Adapter viewPager2Adapter = new ViewPager2Adapter(this);
            ArrayList<Fragment> fragments = new ArrayList<>();
            fragments.add(new FirstFragment());
            fragments.add(new SecondFragment());
            fragments.add(new ThirdFragment());
            viewPager2Adapter.setFragments(fragments);
            viewPager2.setAdapter(viewPager2Adapter);
            tabTitles = new ArrayList<>();
            tabTitles.add("First");
            tabTitles.add("Second");
            tabTitles.add("Third");
            new TabLayoutMediator(tabLayout,viewPager2, this).attach();

        }

        @Override
        public void onConfigureTab(@NonNull TabLayout.Tab tab, int position) {
            tab.setText(tabTitles.get(position));
        }
    }

    //firstfragment.java

    import android.os.Bundle;

    import androidx.fragment.app.Fragment;

    import android.view.LayoutInflater;
    import android.view.View;
    import android.view.ViewGroup;


    public class FirstFragment extends Fragment {



        @Override
        public View onCreateView(LayoutInflater inflater, ViewGroup container,
                                Bundle savedInstanceState) {
            // Inflate the layout for this fragment
            return inflater.inflate(R.layout.fragment_first, container, false);
        }
    }

    //secondfragment.java

    import android.os.Bundle;

    import androidx.fragment.app.Fragment;

    import android.view.LayoutInflater;
    import android.view.View;
    import android.view.ViewGroup;

    public class SecondFragment extends Fragment {

        @Override
        public View onCreateView(LayoutInflater inflater, ViewGroup container,
                                Bundle savedInstanceState) {
            // Inflate the layout for this fragment
            return inflater.inflate(R.layout.fragment_second, container, false);
        }
    }

    //thirdfragment.java

    import android.os.Bundle;

    import androidx.fragment.app.Fragment;
    import androidx.recyclerview.widget.LinearLayoutManager;
    import androidx.recyclerview.widget.RecyclerView;

    import android.view.LayoutInflater;
    import android.view.View;
    import android.view.ViewGroup;


    public class ThirdFragment extends Fragment {

        @Override
        public View onCreateView(LayoutInflater inflater, ViewGroup container,
                                Bundle savedInstanceState) {
            // Inflate the layout for this fragment
            return inflater.inflate(R.layout.fragment_third, container, false);
        }
    }

    //viewpager2adapter.java
    import androidx.annotation.NonNull;
    import androidx.fragment.app.Fragment;
    import androidx.fragment.app.FragmentActivity;
    import androidx.viewpager2.adapter.FragmentStateAdapter;

    import java.util.ArrayList;

    public class ViewPager2Adapter extends FragmentStateAdapter {

        private ArrayList<Fragment> fragments;

        public void setFragments(ArrayList<Fragment> fragments) {
            this.fragments = fragments;
        }

        public ViewPager2Adapter(@NonNull FragmentActivity fragmentActivity) {
            super(fragmentActivity);
        }

        @NonNull
        @Override
        public Fragment createFragment(int position) {
            return fragments.get(position);
        }

        @Override
        public int getItemCount() {
            return fragments.size();
        }
    }
    """
    if(num==1):
        print(xml)
    elif(num==2):
        print(java)
    else:
        print("gandmara")
def firebase(num):

    xml="""
    <?xml version="1.0" encoding="utf-8"?>
    <LinearLayout
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:context=".MainActivity"
        android:orientation="vertical">
        <ImageView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:id="@+id/imageId"/>
        <Button
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Click me"
            android:id="@+id/buttonId"
            android:onClick="doProcess"/>
        <TextView
            android:id="@+id/textId"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            />
    </LinearLayout>
    """
    java="""

    import androidx.annotation.NonNull;
    import androidx.appcompat.app.AppCompatActivity;

    import android.Manifest;
    import android.content.Intent;
    import android.content.pm.PackageManager;
    import android.graphics.Bitmap;
    import android.os.Bundle;
    import android.provider.MediaStore;
    import android.view.View;
    import android.widget.ImageView;
    import android.widget.TextView;
    import android.widget.Toast;

    import com.google.android.gms.tasks.OnFailureListener;
    import com.google.android.gms.tasks.OnSuccessListener;
    import com.google.android.gms.tasks.Task;
    import com.google.firebase.ml.vision.FirebaseVision;
    import com.google.firebase.ml.vision.common.FirebaseVisionImage;
    import com.google.firebase.ml.vision.text.FirebaseVisionText;
    import com.google.firebase.ml.vision.text.FirebaseVisionTextRecognizer;

    import org.jetbrains.annotations.Nullable;

    public class MainActivity extends AppCompatActivity {
        ImageView imageView;
        TextView textView;
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
            imageView=findViewById(R.id.imageId);
            textView=findViewById(R.id.textId);
            if(checkSelfPermission(Manifest.permission.CAMERA)!= PackageManager.PERMISSION_GRANTED){
                requestPermissions(new String[]{Manifest.permission.CAMERA},101);
            }
        }

        public void doProcess(View view){
            Intent intent =new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
            startActivityForResult(intent,101);
        }
        @Override
        protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data){
            super.onActivityResult(requestCode,resultCode,data);
            Bundle bundle = data.getExtras();
            Bitmap bitmap=(Bitmap) bundle.get("data");
            imageView.setImageBitmap(bitmap);
            FirebaseVisionImage firebaseVisionImage =FirebaseVisionImage.fromBitmap(bitmap);
            FirebaseVision firebaseVision=FirebaseVision.getInstance();
            FirebaseVisionTextRecognizer firebaseVisionTextRecognizer=firebaseVision.getOnDeviceTextRecognizer();
            Task<FirebaseVisionText> task=firebaseVisionTextRecognizer.processImage(firebaseVisionImage);
            task.addOnSuccessListener(new OnSuccessListener<FirebaseVisionText>() {
                @Override
                public void onSuccess(FirebaseVisionText firebaseVisionText) {
            String s =firebaseVisionText.getText();
            textView.setText(s);
                }
            });
            task.addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                    Toast.makeText(getApplicationContext(),e.getMessage(),Toast.LENGTH_LONG);
                }
         });
        }
    }
    """
    if(num==1):
        print(xml)
    elif(num==2):
        print(java)
    else:
        print("gandmara")

def location(num):

    xml="""
    <?xml version="1.0" encoding="utf-8"?>
    <RelativeLayout
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:context=".MainActivity">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical">

            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:hint="Country"
                android:textColor="#000"
                android:textSize="20sp"
                android:id="@+id/editCountry"/>

            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:hint="State"
                android:textColor="#000"
                android:textSize="20sp"
                android:id="@+id/editState"/>
            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:hint="City"
                android:textColor="#000"
                android:textSize="20sp"
                android:id="@+id/editCity"/>

            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:hint="Pincode"
                android:textColor="#000"
                android:textSize="20sp"
                android:id="@+id/editPincode"/>

            <Button
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:text="Get Location"
                android:id="@+id/btnShowLocation"/>
        </LinearLayout>
    </RelativeLayout>
    """
    java="""
    import androidx.annotation.NonNull;
    import androidx.appcompat.app.AppCompatActivity;
    import androidx.core.app.ActivityCompat;
    import androidx.core.content.ContextCompat;

    import android.Manifest;
    import android.app.Activity;
    import android.content.Context;
    import android.content.pm.PackageManager;
    import android.location.Address;
    import android.location.Geocoder;
    import android.location.Location;
    import android.location.LocationListener;
    import android.location.LocationManager;
    import android.os.Bundle;
    import android.util.Log;
    import android.view.View;
    import android.widget.Button;
    import android.widget.TextView;
    import android.widget.Toast;
    import java.util.List;
    import java.util.Locale;

    public class MainActivity extends AppCompatActivity implements LocationListener {

        Button btnShowLocation;
        LocationManager locationManager;
        private double latitude;
        private double longitude;
        TextView edit_Country,edit_State,edit_City,edit_Pincode;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);

            edit_Country=findViewById(R.id.editCountry);
            edit_State=findViewById(R.id.editState);
            edit_City=findViewById(R.id.editCity);
            edit_Pincode=findViewById(R.id.editPincode);
            btnShowLocation=findViewById(R.id.btnShowLocation);

            btnShowLocation.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if(ContextCompat.checkSelfPermission(MainActivity.this, Manifest.permission.ACCESS_FINE_LOCATION)!= PackageManager.PERMISSION_GRANTED){
                        ActivityCompat.requestPermissions(MainActivity.this,new String[]{Manifest.permission.ACCESS_FINE_LOCATION},1);
                    }else{
                        detectCurrentLocation();
                    }
                }
            });
        }
        private void detectCurrentLocation(){
            Toast.makeText(this,"Getting your current location",Toast.LENGTH_SHORT).show();
            locationManager=(LocationManager) getSystemService(Context.LOCATION_SERVICE);
            if ((ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) && ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
                return;
            }
            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER,0,0,this);
        }
        @Override
        public void onLocationChanged(Location location) {
        latitude=location.getLatitude();
        longitude=location.getLongitude();
        findAddress();
        }
        private void findAddress(){
            Geocoder geocoder;
            List<Address> addresses;
            geocoder=new Geocoder(this, Locale.getDefault());
            try{
                addresses=geocoder.getFromLocation(latitude,longitude,1);
                String country=addresses.get(0).getCountryName();
                String state=addresses.get(0).getAdminArea();
                String city=addresses.get(0).getLocality();
                String Pincode=addresses.get(0).getPostalCode();

                edit_Country.setText(country);
                edit_State.setText(state);
                edit_City.setText(city);
                edit_Pincode.setText(Pincode);
                Log.d("City",city);
                Log.d("State",state);
                Log.d("Country",country);
                Log.d("Pincode",String.valueOf(Pincode));
            }catch (Exception e){
                Toast.makeText(this,""+e.getMessage(),Toast.LENGTH_SHORT).show();
            }
        }
        @Override
        public void onStatusChanged(String provider,int status,Bundle extras){

        }
        @Override
        public void onProviderEnabled(String provider){

        }
        public void onProviderDisabled(String provider){
            Toast.makeText(this,"Please turn on Location",Toast.LENGTH_SHORT).show();
        }
        @Override
        public void onRequestPermissionsResult(int requestCode,@NonNull String[] permissions,@NonNull int[] grantResults){
            super.onRequestPermissionsResult(requestCode,permissions,grantResults);

            if(requestCode==1){
                if(grantResults.length>0 && grantResults[0]==PackageManager.PERMISSION_GRANTED){
                    detectCurrentLocation();
                }else{
                    Toast.makeText(this,"Permission Denied",Toast.LENGTH_SHORT).show();
                }
           }
        }
    }
    """
    if(num==1):
        print(xml)
    elif(num==2):
        print(java)
    else:
        print("gandmara")
