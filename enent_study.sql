/*declare @j int
set @j=1
declare @file_num int
declare @temp char(10)
declare @temp3 char(10)
select @file_num=max(FileID) from files
while @j<=@file_num
   begin
       select @temp=sheet_name from newfiles where  newfileID=@j
       select @temp3=sheet_name from files where  FileID=@j
       exec('create table ' +@temp+ '(ID int identity(1,1) not null, ���� char(10),�۸� float,������ float)')   --ʹ�ñ�������̬������
       insert into @temp(����,�۸�,������) select ����,�۸�,������ from @temp3
       set @j=@j+1
       --drop table sh1
       --delete from new_sh1 where ������ is null
   end
   */
declare @temp1 char(10)
declare @temp2 char(10)
set @temp1='new_ch2'
set @temp2='sh2'
--select @temp=sheet_name from newfiles where  newfileID=1

--exec('create table ' +@temp+ '(ID int identity(1,1) not null, ���� char(10),�۸� float,������ float)')   --ʹ�ñ�������̬������
--exec('insert into ' + @temp1(����,�۸�,������)+ ' select ' + '(����,�۸�,������)' + ' from ' +@temp2)
--insert into @temp1(����,�۸�,������) select ����,�۸�,������ from @temp2
--exec('insert into ' + @temp1'(����,�۸�,������)' + 'values('ji',25.3,2563)')
--exec('select * into #tem from ' +@temp2)
--exec('insert into ' +@temp1+'(����,�۸�,������) select ����,�۸�,������ from #tem')
--select * from #tem 
exec('insert into' + @temp1+' (����,�۸�,������)' + ' select ' + ' (����,�۸�,������) ' + 'from' +@temp2)  --ʹ��һ����ʱ�����ݸ��Ƶ��Ա�����Ϊ���Ƶı���




/*
declare @i int
declare @n int
declare @temp1 float
declare @temp2 float
declare @sheet_name char(10)
while sheet_ID<=max_ID
   select @sheet_name=name from name_sheet where ID=sheet_ID
   select @n=max(ID) from new_sh1
   set @i=1
   while @i<@n
      begin
         select @temp1=�۸� from @sheet_name where ID=@i
         select @temp2=�۸� from @sheet_name where ID=@i+1
         update new_sheet set shouyi=((@temp2-@temp1)/@temp1) where ID=@i
         set @i=@i+1
     end
end
*/
  


